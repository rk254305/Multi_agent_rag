"""
Price Normalizer Tool

Provides utilities to clean and standardize price values
"""

from app.utils.logger import logger


def normalize_price(price) -> float:
    """
    Normalize price into float

    :param price: Raw price (string/int/float)
    :return: Clean float price
    """

    logger.info(f"Normalizing price: {price}")

    if price is None:
        logger.warning("Price is None")
        return 0.0

    try:
        # Convert to string for cleaning
        price_str = str(price)

        # Remove currency symbols and commas
        cleaned = (
            price_str.replace("₹", "")
                     .replace(",", "")
                     .replace("INR", "")
                     .strip()
        )

        normalized = float(cleaned)

        logger.info(f"Normalized price: {normalized}")

        return normalized

    except Exception as e:
        logger.error(f"Price normalization failed: {e}")
        return 0.0
