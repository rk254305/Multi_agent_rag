"""
Embeddings Module

Provides embedding model used in the RAG pipeline.
Supports multiple providers (OpenAI, Ollama, HuggingFace).
"""

from app.utils.logger import logger


def get_embeddings(provider: str = "huggingface"):
    """
    Return embeddings model based on provider

    :param provider: openai | ollama | huggingface
    :return: Embeddings object
    """

    logger.info(f"Loading embeddings provider: {provider}")

    if provider == "openai":
        from langchain_openai import OpenAIEmbeddings

        embeddings = OpenAIEmbeddings()
        logger.info("OpenAI embeddings loaded")

    elif provider == "ollama":
        from langchain_ollama import OllamaEmbeddings

        embeddings = OllamaEmbeddings(model="nomic-embed-text")
        logger.info("Ollama embeddings loaded")

    else:  # Default → HuggingFace
        from langchain_community.embeddings import HuggingFaceEmbeddings

        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        logger.info("HuggingFace embeddings loaded")

    return embeddings
