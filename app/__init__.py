"""
Multi-Agent RAG Price Comparison System

Core application package
"""

# Optional centralized exports

from app.agents import (
    RouterAgent,
    AmazonAgent,
    FlipkartAgent,
    ShopifyAgent,
    ComparisonAgent,
    ResponseAgent,
)

from app.models import Product
from app.tools import compare_prices, normalize_price
from app.utils import logger

__all__ = [
    # Agents
    "RouterAgent",
    "AmazonAgent",
    "FlipkartAgent",
    "ShopifyAgent",
    "ComparisonAgent",
    "ResponseAgent",

    # Models
    "Product",

    # Tools
    "compare_prices",
    "normalize_price",

    # Utils
    "logger",
]
