from dotenv import load_dotenv
import os

load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


# ---------------------------------------------------------------------------
# 1. CONTEXT: The cricket history text (source of truth for the LLM)
# ---------------------------------------------------------------------------
CRICKET_CONTEXT = """
The sport of cricket has a known history beginning in the late 16th century England.
It became an established sport in the country in the 18th century and developed globally
in the 19th and 20th centuries. International matches have been played since the
19th-century and formal Test cricket matches are considered to date from 1877. Cricket
is the world's second most popular spectator sport, after association football (soccer).

Cricket is governed by the International Cricket Council (ICC), which has over one
hundred countries and territories in membership, though only twelve currently play
Test cricket.

The game's rules are defined in the "Laws of cricket". The game has various formats,
ranging from T-10 (Ten-10) played in around 90 minutes to Test matches, which can last
up to five days.
""".strip()

# ---------------------------------------------------------------------------
# 2. QUESTION: What we want the LLM to answer
# ---------------------------------------------------------------------------
QUESTION = (
    "When were formal Test cricket matches first considered to have begun, "
    "and which organization currently governs the sport worldwide?"
)


def main() -> None:
    # Show configuration
    base_url = os.getenv("OPENAI_BASE_URL", "not set")
    model = os.getenv("OLLAMA_MODEL", "not set")
    print(f"LLM Provider: Ollama (Docker) ({base_url})")
    print(f"Model: {model}\n")

    # -------------------------------------------------------------------
    # 3. PROMPT TEMPLATE: Tells the LLM to answer ONLY from the context
    # -------------------------------------------------------------------
    prompt = ChatPromptTemplate.from_template(
        "Answer the question using only the information in the context below.\n\n"
        "Context:\n{context}\n\n"
        "Question: {question}\n\n"
        "Answer:"
    )

    # -------------------------------------------------------------------
    # 4. LLM: Ollama running in Docker via OpenAI-compatible API
    # -------------------------------------------------------------------
    llm = ChatOpenAI(
        model=os.getenv("OLLAMA_MODEL", "llama3.2"),
        temperature=0,
        base_url=os.getenv("OPENAI_BASE_URL", "http://localhost:11434/v1"),
        api_key=os.getenv("OPENAI_API_KEY", "ollama"),
    )

    # -------------------------------------------------------------------
    # 5. CHAIN: prompt → LLM → string output
    # -------------------------------------------------------------------
    chain = prompt | llm | StrOutputParser()

    # -------------------------------------------------------------------
    # 6. RUN: Pass context + question, print the answer
    # -------------------------------------------------------------------
    answer = chain.invoke({"context": CRICKET_CONTEXT, "question": QUESTION})

    print("\n--- LLM Answer ---")
    print(answer)


# ---------------------------------------------------------------------------
# 7. BASIC TOOL DEMONSTRATION
# ---------------------------------------------------------------------------
def demo_tool() -> None:
    from langchain_course.tools import count_words

    # --- Run the tool directly ------------------------------------------------
    sample = "LangChain makes building LLM apps simple"
    result = count_words.invoke(sample)

    print("--- Tool demo ---")
    print(f"Input:    {sample!r}")
    print(f"Output:   {result}")
    print(f"Name:     {count_words.name}")
    print(f"Desc:     {count_words.description}")
    print(f"Args:     {count_words.args}")


if __name__ == "__main__":
    # Always run the tool demo (no external service required).
    demo_tool()
    print()

    # Attempt the existing LLM chain; skip gracefully if Ollama isn't running.
    try:
        main()
    except Exception as exc:  # noqa: BLE001
        print(f"Skipping LLM chain (Ollama not reachable): {type(exc).__name__}")