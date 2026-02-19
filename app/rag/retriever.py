"""
Retriever Module

Provides retrieval interface for the RAG pipeline.
"""

from app.rag.vectorstore import get_vectorstore
from app.utils.logger import logger


def get_retriever(search_type: str = "similarity", k: int = 4):
    """
    Create and return retriever

    :param search_type: similarity | mmr
    :param k: Number of documents to retrieve
    :return: Retriever object
    """

    logger.info("Initializing retriever...")

    vectorstore = get_vectorstore()

    retriever = vectorstore.as_retriever(
        search_type=search_type,
        search_kwargs={"k": k}
    )

    logger.info(f"Retriever ready (type={search_type}, k={k})")

    return retriever


def retrieve_documents(query: str):
    """
    Retrieve documents based on query

    :param query: User query
    :return: List of Documents
    """

    logger.info(f"Retrieving documents for query: {query}")

    retriever = get_retriever()
    docs = retriever.get_relevant_documents(query)

    logger.info(f"{len(docs)} documents retrieved")

    return docs
