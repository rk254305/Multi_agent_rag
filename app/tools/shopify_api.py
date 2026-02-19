"""
Shopify API Tool

Fetches product data from Shopify stores via products.json endpoint
"""

import requests
from typing import List
from app.models.product import Product
from app.tools.price_normalizer import normalize_price
from app.utils.logger import logger


class ShopifyAPI:
    def __init__(self):
        logger.info("ShopifyAPI tool initialized")

    def fetch_products(self, store_url: str) -> List[Product]:
        """
        Fetch products from Shopify store

        :param store_url: Shopify store URL (without /products.json)
        :return: List of Product objects
        """

        logger.info(f"Fetching Shopify products from: {store_url}")

        endpoint = f"{store_url}/products.json"

        try:
            response = requests.get(endpoint)
            data = response.json()

            products = []

            for item in data.get("products", []):
                title = item.get("title")
                variants = item.get("variants", [])

                if not variants:
                    continue

                # Use first variant price
                variant = variants[0]
                raw_price = variant.get("price")

                price = normalize_price(raw_price)

                products.append(
                    Product(
                        source="Shopify",
                        title=title,
                        price=price,
                        url=f"{store_url}/products/{item.get('handle')}",
                        availability="Unknown"
                    )
                )

            logger.info(f"{len(products)} Shopify products fetched")

            return products

        except Exception as e:
            logger.error(f"ShopifyAPI error: {e}")
            return []
