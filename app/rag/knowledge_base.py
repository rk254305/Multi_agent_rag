"""
Knowledge Base Module

Handles document ingestion and updates for the RAG pipeline.
"""

from typing import List
from langchain_core.documents import Document
from app.utils.logger import logger


def build_documents(products: List[dict]) -> List[Document]:
    """
    Convert product data into LangChain Documents

    :param products: List of product dictionaries
    :return: List of Documents
    """

    logger.info("Building documents for knowledge base...")

    documents = []

    for p in products:
        content = f"""
        Product: {p.get('title')}
        Source: {p.get('source')}
        Price: ₹{p.get('price')}
        Availability: {p.get('availability')}
        URL: {p.get('url')}
        """

        documents.append(
            Document(
                page_content=content.strip(),
                metadata={
                    "source": p.get("source"),
                    "price": p.get("price"),
                    "url": p.get("url"),
                }
            )
        )

    logger.info(f"{len(documents)} documents created")

    return documents


def add_to_knowledge_base(vectorstore, documents: List[Document]):
    """
    Add documents to vector database

    :param vectorstore: FAISS / Chroma instance
    :param documents: List of Documents
    """

    logger.info("Adding documents to vectorstore...")

    vectorstore.add_documents(documents)

    logger.info("Documents successfully added to knowledge base")
