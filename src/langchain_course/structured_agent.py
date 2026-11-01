"""
Structured-output agents with LangChain.

Builds LangChain *agents* (LLM that can choose and call tools) that return
*structured output* (typed Pydantic object instead of free text).

Conventions matching this course:
  * LLM: langchain_openai.ChatOpenAI
  * Tools: langchain_core.tools.tool decorator
  * Schema: pydantic.BaseModel

Two patterns:
  A. with_structured_output — LLM returns a Pydantic object (no tools).
  B. create_agent with response_format — agent + tools + structured final answer.
"""

from __future__ import annotations

import os
from typing import List

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

load_dotenv()


class ResearchAnswer(BaseModel):
    """The structured shape of the agent's final answer."""

    topic: str = Field(..., description="The subject that was researched.")
    summary: str = Field(..., description="A concise one-paragraph summary.")
    key_points: List[str] = Field(
        ..., description="3-5 bullet points capturing the most important facts."
    )
    confidence: float = Field(
        ..., ge=0.0, le=1.0, description="Confidence score between 0 and 1."
    )
    sources: List[str] = Field(
        default_factory=list, description="Any sources referenced (if applicable)."
    )


@tool
def count_words(text: str) -> int:
    """Count the number of words in the given text."""
    return len(text.split())


@tool
def fake_search(query: str) -> str:
    """Pretend to search the web for a query and return a snippet."""
    return (
        f"Search results for '{query}': The Eiffel Tower is located in Paris, "
        "France. It was completed in 1889."
    )


def get_llm() -> ChatOpenAI:
    return ChatOpenAI(
        model=os.getenv("OLLAMA_MODEL", "llama3.2"),
        temperature=0,
        base_url=os.getenv("OPENAI_BASE_URL", "http://localhost:11434/v1"),
        api_key=os.getenv("OPENAI_API_KEY", "ollama"),
    )


def pattern_a_structured_llm_only() -> ResearchAnswer:
    """
    Simplest structured output: LLM returns a Pydantic object directly.

    Use when you do NOT need the agent to pick/call tools — you just want typed
    output from the model.
    """
    llm = get_llm()
    structured_llm = llm.with_structured_output(ResearchAnswer)

    prompt = ChatPromptTemplate.from_messages(
        [
            SystemMessage(
                content=(
                    "You are a research assistant. Answer using ONLY the provided "
                    "context. Return your response as a structured ResearchAnswer."
                )
            ),
            HumanMessage(
                content=(
                    "Context: The Eiffel Tower is an iron lattice tower in Paris, "
                    "France. It was designed by Gustave Eiffel and completed in 1889 "
                    "for the Exposition Universelle. It stands 330 metres tall.\n\n"
                    "Question: Where is the Eiffel Tower and when was it completed?"
                )
            ),
        ]
    )

    chain = prompt | structured_llm
    return chain.invoke({})



def pattern_b_agent_with_structured_output() -> ResearchAnswer:
    """
    Full agent with tools whose FINAL answer is structured.

    The agent reasons about which tool to call, calls it, then produces a final
    answer conforming to ResearchAnswer.
    """
    llm = get_llm()
    tools = [count_words, fake_search]

    # create_agent is the LangGraph-based agent factory (langchain 1.4.x).
    # response_format coerces the agent's final output into the Pydantic model.
    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt=(
            "You are a helpful research assistant. Use the available tools when "
            "useful, then answer the user's question. Return your final answer as "
            "a structured ResearchAnswer object."
        ),
        response_format=ResearchAnswer,
    )

    result = agent.invoke(
        {
            "messages": [
                HumanMessage(
                    content=(
                        "Search for information about the Eiffel Tower, then tell "
                        "me where it is, when it was completed, and give me a short "
                        "summary with key points."
                    )
                )
            ]
        }
    )

    # The structured answer lives under the "structured_response" key.
    return result["structured_response"]


def main() -> None:
    print("=" * 60)
    print("PATTERN A: with_structured_output (no tools)")
    print("=" * 60)
    try:
        answer_a = pattern_a_structured_llm_only()
        print(f"Topic:        {answer_a.topic}")
        print(f"Summary:      {answer_a.summary}")
        print(f"Key points:   {answer_a.key_points}")
        print(f"Confidence:   {answer_a.confidence}")
        print(f"Sources:      {answer_a.sources}")
        print(f"Type:         {type(answer_a).__name__}")
    except Exception as exc:  # noqa: BLE001
        print(f"(Skipped — LLM not reachable): {type(exc).__name__}: {exc}")

    print()
    print("=" * 60)
    print("PATTERN B: create_agent + tools + response_format")
    print("=" * 60)
    try:
        answer_b = pattern_b_agent_with_structured_output()
        print(f"Topic:        {answer_b.topic}")
        print(f"Summary:      {answer_b.summary}")
        print(f"Key points:   {answer_b.key_points}")
        print(f"Confidence:   {answer_b.confidence}")
        print(f"Sources:      {answer_b.sources}")
        print(f"Type:         {type(answer_b).__name__}")
    except Exception as exc:  # noqa: BLE001
        print(f"(Skipped — LLM not reachable): {type(exc).__name__}: {exc}")

    # Tool demo that works WITHOUT an LLM (matches main.py convention).
    print()
    print("=" * 60)
    print("TOOL DEMO (no LLM required)")
    print("=" * 60)
    sample = "LangChain makes building LLM apps simple"
    print(f"Input:    {sample!r}")
    print(f"Output:   {count_words.invoke(sample)}")
    print(f"Name:     {count_words.name}")
    print(f"Desc:     {count_words.description}")


if __name__ == "__main__":
    main()
