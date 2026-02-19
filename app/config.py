"""
Configuration Module

Handles environment variables and global settings
"""

import os
from dotenv import load_dotenv
from app.utils.logger import logger

# Load .env file
load_dotenv()


# 🔐 API Keys
FLIPKART_APP_ID = os.getenv("FLIPKART_APP_ID")
FLIPKART_APP_SECRET = os.getenv("FLIPKART_APP_SECRET")

AMAZON_API_KEY = os.getenv("AMAZON_API_KEY")
SHOPIFY_STORE_URL = os.getenv("SHOPIFY_STORE_URL")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")


# ⚙️ App Settings
DEFAULT_CURRENCY = "INR"
VECTORSTORE_DIR = "data/vectorstore"


def validate_config():
    """
    Validate critical environment variables
    """

    logger.info("Validating configuration...")

    if not FLIPKART_APP_ID or not FLIPKART_APP_SECRET:
        logger.warning("Flipkart API credentials not set")

    if not AMAZON_API_KEY:
        logger.warning("Amazon API key not set")

    if not OPENAI_API_KEY and not GROQ_API_KEY:
        logger.warning("No LLM API key configured")

    logger.info("Configuration validation completed")
