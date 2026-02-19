"""
Vector Store Module

Handles vector database initialization and persistence.
Supports FAISS (default) and Chroma.
"""

from langchain_community.vectorstores import FAISS
from langchain_community.vectorstores import Chroma
from app.rag.embeddings import get_embeddings
from app.utils.logger import logger
import os

# Directory for persistent storage
VECTORSTORE_DIR = "data/vectorstore"


def get_vectorstore(store_type: str = "faiss"):
    """
    Initialize or load vector store

    :param store_type: faiss | chroma
    :return: Vector store instance
    """

    logger.info(f"Loading vectorstore (type={store_type})")

    embeddings = get_embeddings()

    os.makedirs(VECTORSTORE_DIR, exist_ok=True)

    if store_type == "chroma":
        vectorstore = Chroma(
            persist_directory=VECTORSTORE_DIR,
            embedding_function=embeddings
        )
        logger.info("Chroma vectorstore ready")

    else:  # Default → FAISS
        index_path = os.path.join(VECTORSTORE_DIR, "faiss_index")

        if os.path.exists(index_path):
            vectorstore = FAISS.load_local(
                index_path,
                embeddings,
                allow_dangerous_deserialization=True
            )
            logger.info("FAISS index loaded from disk")
        else:
            vectorstore = FAISS.from_texts(
                texts=["Initial knowledge base"],
                embedding=embeddings
            )
            logger.info("New FAISS index created")

        # Save FAISS index
        vectorstore.save_local(index_path)

    return vectorstore


def save_vectorstore(vectorstore, store_type: str = "faiss"):
    """
    Persist vector store to disk

    :param vectorstore: FAISS / Chroma instance
    """

    logger.info("Saving vectorstore...")

    if store_type == "chroma":
        vectorstore.persist()
        logger.info("Chroma vectorstore persisted")

    else:
        index_path = os.path.join(VECTORSTORE_DIR, "faiss_index")
        vectorstore.save_local(index_path)
        logger.info("FAISS index saved")
