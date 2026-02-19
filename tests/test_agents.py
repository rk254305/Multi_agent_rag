"""
Agent Tests

Tests for RouterAgent and ComparisonAgent
"""

from app.agents.router_agent import RouterAgent
from app.agents.comparison_agent import ComparisonAgent
from app.models import Product


# ✅ Test RouterAgent
def test_router_comparison():
    router = RouterAgent()
    assert router.route("Compare iPhone 15 prices") == "comparison"


def test_router_amazon():
    router = RouterAgent()
    assert router.route("Check price on Amazon") == "amazon"


def test_router_flipkart():
    router = RouterAgent()
    assert router.route("Flipkart price of Samsung") == "flipkart"


def test_router_price_lookup():
    router = RouterAgent()
    assert router.route("What is the price of MacBook") == "price_lookup"


# ✅ Test ComparisonAgent
def test_comparison_agent_cheapest():
    agent = ComparisonAgent()

    products = [
        Product(source="Amazon", title="Product A", price=70000, url="x"),
        Product(source="Flipkart", title="Product B", price=68000, url="y"),
    ]

    result = agent.compare(products)

    assert result["cheapest"]["price"] == 68000
    assert result["highest"]["price"] == 70000


def test_comparison_agent_difference():
    agent = ComparisonAgent()

    products = [
        Product(source="Amazon", title="A", price=80000, url="x"),
        Product(source="Flipkart", title="B", price=75000, url="y"),
    ]

    result = agent.compare(products)

    assert result["price_difference"] == 5000


# ✅ Test Empty Input Handling
def test_comparison_agent_empty():
    agent = ComparisonAgent()

    result = agent.compare([])

    assert "error" in result
