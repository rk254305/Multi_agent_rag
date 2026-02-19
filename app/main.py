"""
Main Application Entry Point

Coordinates agents, tools, and APIs
"""

from app.agents import (
    RouterAgent,
    AmazonAgent,
    FlipkartAgent,
    ShopifyAgent,
    ComparisonAgent,
    ResponseAgent,
)

from app.tools import compare_prices
from app.config import validate_config
from app.utils.logger import logger


def main():
    logger.info("🚀 Starting Multi-Agent RAG Price System")

    # Validate config
    validate_config()

    # Initialize agents
    router = RouterAgent()
    amazon_agent = AmazonAgent()
    flipkart_agent = FlipkartAgent()
    shopify_agent = ShopifyAgent()

    comparison_agent = ComparisonAgent()
    response_agent = ResponseAgent()

    # User input
    query = input("\n🔎 Enter your query: ")

    # Route query
    route = router.route(query)

    products = []

    # 🎯 Routing Logic
    if route == "amazon":
        products.extend(amazon_agent.search_product(query))

    elif route == "flipkart":
        products.extend(flipkart_agent.search_product(query))

    elif route == "comparison":
        logger.info("Running multi-platform comparison")

        products.extend(amazon_agent.search_product(query))
        products.extend(flipkart_agent.search_product(query))
        products.extend(shopify_agent.search_product(query))

    elif route == "price_lookup":
        logger.info("Running price lookup across platforms")

        products.extend(amazon_agent.search_product(query))
        products.extend(flipkart_agent.search_product(query))

    else:
        logger.info("General query → defaulting to comparison")

        products.extend(amazon_agent.search_product(query))
        products.extend(flipkart_agent.search_product(query))

    # 🛒 Show fetched products
    logger.info(f"{len(products)} products retrieved")

    for p in products:
        print(f"\n• {p.title} | {p.source} | ₹{p.price}")

    # 📊 Compare prices
    comparison_result = compare_prices(products)

    # 💬 Format response
    response = response_agent.format_comparison(comparison_result)

    print("\n" + "=" * 50)
    print(response)
    print("=" * 50)


if __name__ == "__main__":
    main()
