"""
Shopify Agent

Responsible for retrieving product data from Shopify stores.
Can integrate with Shopify Storefront API or public products.json endpoint.
"""

from typing import List
from app.models.product import Product
from app.utils.logger import logger


class ShopifyAgent:
    def __init__(self, api_client=None):
        """
        Initialize ShopifyAgent

        :param api_client: Optional Shopify API client
        """
        self.api_client = api_client
        logger.info("ShopifyAgent initialized")

    def search_product(self, product_name: str) -> List[Product]:
        """
        Search for a product in Shopify store(s)

        :param product_name: Product name
        :return: List of Product objects
        """

        logger.info(f"Searching Shopify for: {product_name}")

        # 🚧 Placeholder (replace with real API/store calls later)
        dummy_data = [
            Product(
                source="Shopify",
                title=f"{product_name} (Sample Store Listing)",
                price=0.0,
                url="https://example-store.myshopify.com",
                availability="Unknown"
            )
        ]

        logger.info("Shopify search completed (placeholder)")

        return dummy_data

    def fetch_from_store(self, store_url: str) -> List[Product]:
        """
        Fetch products from a specific Shopify store

        :param store_url: Shopify store URL
        :return: List of Product objects
        """

        logger.info(f"Fetching products from Shopify store: {store_url}")

        # 🚧 Placeholder logic
        return []
