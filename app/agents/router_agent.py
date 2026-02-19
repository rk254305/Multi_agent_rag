"""
Router Agent

Responsible for analyzing user queries and routing them
to appropriate agents (Amazon, Flipkart, Comparison, etc.)
"""

from app.utils.logger import logger


class RouterAgent:
    def __init__(self):
        logger.info("RouterAgent initialized")

    def route(self, query: str) -> str:
        """
        Determine user intent from query

        :param query: User input
        :return: Route निर्णय (agent/action)
        """

        logger.info(f"Routing query: {query}")

        query_lower = query.lower()

        # 🎯 Intent Detection (Rule-Based)
        if "compare" in query_lower:
            route = "comparison"

        elif "amazon" in query_lower:
            route = "amazon"

        elif "flipkart" in query_lower:
            route = "flipkart"

        elif "price" in query_lower:
            route = "price_lookup"

        else:
            route = "general"

        logger.info(f"Query routed to: {route}")

        return route
