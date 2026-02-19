"""
API Tool Tests

Tests API wrappers without making real HTTP calls
"""

from app.tools.amazon_api import AmazonAPI
from app.tools.flipkart_api import FlipkartAPI
from app.tools.shopify_api import ShopifyAPI


# ✅ Initialization Tests
def test_amazon_api_init():
    api = AmazonAPI()
    assert api is not None


def test_flipkart_api_init():
    api = FlipkartAPI()
    assert api is not None


def test_shopify_api_init():
    api = ShopifyAPI()
    assert api is not None
