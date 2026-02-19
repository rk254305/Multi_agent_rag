"""
Comparison Agent

Responsible for analyzing and comparing product prices
from multiple sources (Amazon, Flipkart, Shopify, etc.)
"""

from typing import List, Dict
from app.models.product import Product
from app.utils.logger import logger


class ComparisonAgent:
    def __init__(self):
        logger.info("ComparisonAgent initialized")

    def compare(self, products: List[Product]) -> Dict:
        """
        Compare product prices

        :param products: List of Product objects
        :return: Comparison summary
        """

        logger.info("Starting price comparison...")

        if not products:
            logger.warning("No products provided for comparison")
            return {"error": "No products to compare"}

        # Find cheapest & highest
        cheapest = min(products, key=lambda p: p.price)
        highest = max(products, key=lambda p: p.price)

        difference = highest.price - cheapest.price

        result = {
            "cheapest": cheapest.dict(),
            "highest": highest.dict(),
            "price_difference": difference,
            "total_sources": len(set(p.source for p in products))
        }

        logger.info("Price comparison completed")

        return result

    def best_deal(self, products: List[Product]) -> Product:
        """
        Return cheapest product

        :param products: List of Product objects
        :return: Product
        """

        logger.info("Calculating best deal...")

        if not products:
            logger.warning("No products available")
            return None

        best = min(products, key=lambda p: p.price)

        logger.info(f"Best deal found: {best.title} at ₹{best.price}")

        return best
