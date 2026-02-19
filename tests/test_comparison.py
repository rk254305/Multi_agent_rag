"""
Comparison Logic Tests
"""

from app.tools.price_compare import compare_prices, find_cheapest, price_difference
from app.models import Product


# ✅ Test Cheapest Product
def test_find_cheapest():
    products = [
        Product(source="Amazon", title="Product A", price=50000, url="x"),
        Product(source="Flipkart", title="Product B", price=45000, url="y"),
        Product(source="Shopify", title="Product C", price=47000, url="z"),
    ]

    cheapest = find_cheapest(products)

    assert cheapest.price == 45000
    assert cheapest.source == "Flipkart"


# ✅ Test Full Comparison
def test_compare_prices():
    products = [
        Product(source="Amazon", title="A", price=60000, url="x"),
        Product(source="Flipkart", title="B", price=55000, url="y"),
    ]

    result = compare_prices(products)

    assert result["cheapest"]["price"] == 55000
    assert result["highest"]["price"] == 60000
    assert result["price_difference"] == 5000


# ✅ Test Price Difference Function
def test_price_difference():
    products = [
        Product(source="Amazon", title="A", price=80000, url="x"),
        Product(source="Flipkart", title="B", price=75000, url="y"),
    ]

    diff = price_difference(products)

    assert diff == 5000


# ✅ Edge Case → Single Product
def test_single_product():
    products = [
        Product(source="Amazon", title="Only Product", price=70000, url="x"),
    ]

    result = compare_prices(products)

    assert result["cheapest"]["price"] == 70000
    assert result["highest"]["price"] == 70000
    assert result["price_difference"] == 0


# ✅ Edge Case → Empty List
def test_empty_products():
    result = compare_prices([])
    assert "error" in result
