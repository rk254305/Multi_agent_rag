"""
Amazon Agent

Responsible for retrieving product data from Amazon via API integration.
"""

from typing import List
from app.models.product import Product
from app.utils.logger import logger


class AmazonAgent:
    def __init__(self, api_client=None):
        """
        Initialize AmazonAgent

        :param api_client: Optional API client (Rainforest / PA-API / SerpAPI)
        """
        self.api_client = api_client
        logger.info("AmazonAgent initialized")

    def search_product(self, product_name: str) -> List[Product]:
        """
        Search for a product on Amazon

        :param product_name: Name of the product
        :return: List of Product objects
        """

        logger.info(f"Searching Amazon for: {product_name}")

        # 🚧 Placeholder logic (replace with API call later)
        dummy_data = [
            Product(
                source="Amazon",
                title=f"{product_name} (Sample Listing 1)",
                price=0.0,
                url="https://amazon.in",
                availability="Unknown"
            )
        ]

        logger.info("Amazon search completed (placeholder)")

        return dummy_data

    def get_price(self, product_name: str) -> float:
        """
        Retrieve product price (optional helper)

        :param product_name: Product name
        :return: Price
        """

        logger.info(f"Fetching Amazon price for: {product_name}")

        # 🚧 Placeholder
        return 0.0
