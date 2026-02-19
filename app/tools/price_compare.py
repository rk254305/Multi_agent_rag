"""
Price Comparison Tool

Provides helper functions to compare product prices
"""

from typing import List, Dict, Optional
from app.models.product import Product
from app.utils.logger import logger


def compare_prices(products: List[Product]) -> Dict:
    """
    Compare product prices

    :param products: List of Product objects
    :return: Comparison result
    """

    logger.info("Running price comparison tool...")

    if not products:
        logger.warning("No products provided for comparison")
        return {"error": "No products to compare"}

    try:
        cheapest = min(products, key=lambda p: p.price)
        highest = max(products, key=lambda p: p.price)

        difference = highest.price - cheapest.price

        result = {
            "cheapest": cheapest.dict(),
            "highest": highest.dict(),
            "price_difference": difference,
            "total_products": len(products),
            "sources_compared": list(set(p.source for p in products))
        }

        logger.info("Price comparison completed")

        return result

    except Exception as e:
        logger.error(f"Comparison error: {e}")
        return {"error": str(e)}


def find_cheapest(products: List[Product]) -> Optional[Product]:
    """
    Return cheapest product

    :param products: List of Product objects
    :return: Product or None
    """

    logger.info("Finding cheapest product...")

    if not products:
        logger.warning("Empty product list")
        return None

    cheapest = min(products, key=lambda p: p.price)

    logger.info(f"Cheapest product: {cheapest.title} → ₹{cheapest.price}")

    return cheapest


def price_difference(products: List[Product]) -> float:
    """
    Calculate price difference between highest & lowest

    :param products: List of Product objects
    :return: Price difference
    """

    if not products:
        return 0.0

    lowest = min(products, key=lambda p: p.price)
    highest = max(products, key=lambda p: p.price)

    return highest.price - lowest.price
