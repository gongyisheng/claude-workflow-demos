"""LLM / AI SDK dependencies.

One function per dependency: anthropic, openai, tiktoken, langchain,
llama-index (llama_index).
"""

import anthropic
import openai
import tiktoken
import langchain
import llama_index


def anthropic_client(api_key: str = "sk-ant-demo"):
    """anthropic: build an Anthropic API client."""
    return anthropic.Anthropic(api_key=api_key)


def openai_client(api_key: str = "sk-demo"):
    """openai: build an OpenAI API client."""
    return openai.OpenAI(api_key=api_key)


def count_tokens(text: str, encoding: str = "cl100k_base") -> int:
    """tiktoken: count the tokens in a string."""
    enc = tiktoken.get_encoding(encoding)
    return len(enc.encode(text))


def langchain_version() -> str:
    """langchain: report the installed langchain version."""
    return langchain.__version__


def llama_index_version() -> str:
    """llama-index: report the installed llama_index version."""
    return llama_index.__version__
