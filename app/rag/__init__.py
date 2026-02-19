"""
RAG Package (Retrieval-Augmented Generation)

Contains components responsible for:
- Embeddings
- Vector store
- Retrieval logic
"""

from .embeddings import get_embeddings
from .vectorstore import get_vectorstore
from .retriever import get_retriever

__all__ = [
    "get_embeddings",
    "get_vectorstore",
    "get_retriever",
]
