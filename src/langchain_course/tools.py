"""Basic LangChain tools for the course.

A LangChain ``tool`` is just a Python function decorated with ``@tool``.
LangChain automatically:
  * derives the tool name from the function name,
  * derives the description from the docstring,
  * builds an input schema (JSON Schema) from the type hints,
  * exposes a standard ``invoke`` / ``ainvoke`` / ``call`` interface so the
    tool can be used standalone or bound to an LLM for tool calling.
"""
from __future__ import annotations

from langchain_core.tools import tool


@tool
def count_words(text: str) -> int:
    """Count the number of words in the given text."""
    return len(text.split())
