"""
Flipkart API Tool

Handles Flipkart Affiliate API communication
"""

import requests
from typing import List
from app.models.product import Product
from app.utils.logger import logger
from app.config import FLIPKART_APP_ID, FLIPKART_APP_SECRET


class FlipkartAPI:
    def __init__(self):
        logger.info("FlipkartAPI tool initialized")

    def search_products(self, product_name: str, count: int = 3) -> List[Product]:
        """
        Search products on Flipkart

        :param product_name: Product query
        :param count: Number of results
        :return: List of Product objects
        """

        logger.info(f"FlipkartAPI searching for: {product_name}")

        url = "https://affiliate-api.flipkart.net/affiliate/search/json"

        headers = {
            "Fk-Affiliate-Id": FLIPKART_APP_ID,
            "Fk-Affiliate-Token": FLIPKART_APP_SECRET
        }

        params = {
            "query": product_name,
            "resultCount": count
        }

        try:
            response = requests.get(url, headers=headers, params=params)
            data = response.json()

            products = []

            for item in data.get("products", []):
                info = item.get("productBaseInfoV1", {})

                title = info.get("title")
                price_info = info.get("flipkartSellingPrice", {})
                price = price_info.get("amount")
                product_url = info.get("productUrl")

                if title and price and product_url:
                    products.append(
                        Product(
                            source="Flipkart",
                            title=title,
                            price=float(price),
                            url=product_url,
                            availability="In Stock"
                        )
                    )

            logger.info(f"{len(products)} Flipkart products fetched")

            return products

        except Exception as e:
            logger.error(f"FlipkartAPI error: {e}")
            return []
