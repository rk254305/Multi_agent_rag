"""
Helpers Module

Common reusable helper functions
"""

from app.utils.logger import logger


def format_currency(price: float, currency: str = "INR") -> str:
    """
    Format price with currency symbol

    :param price: Numeric price
    :param currency: Currency code
    :return: Formatted string
    """

    logger.info(f"Formatting currency: {price} {currency}")

    if currency == "INR":
        return f"₹{price:,.2f}"

    return f"{currency} {price:,.2f}"


def safe_float(value, default: float = 0.0) -> float:
    """
    Safely convert value to float

    :param value: Any value
    :param default: Default if conversion fails
    :return: Float
    """

    try:
        return float(value)
    except Exception:
        logger.warning(f"safe_float failed for value: {value}")
        return default


def clean_text(text: str) -> str:
    """
    Clean unwanted whitespace

    :param text: Raw text
    :return: Cleaned text
    """

    if not text:
        return ""

    cleaned = " ".join(text.split())
    logger.info(f"Cleaned text: {cleaned}")

    return cleaned
