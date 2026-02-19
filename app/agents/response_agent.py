"""
Response Agent

Responsible for generating human-readable responses
based on comparison and retrieval results.
"""

from typing import Dict
from app.utils.logger import logger


class ResponseAgent:
    def __init__(self, llm=None):
        """
        Initialize ResponseAgent

        :param llm: Optional LLM (Groq / OpenAI / Ollama)
        """
        self.llm = llm
        logger.info("ResponseAgent initialized")

    def format_comparison(self, comparison_result: Dict) -> str:
        """
        Format comparison output into readable text

        :param comparison_result: Output from ComparisonAgent
        :return: Formatted string
        """

        logger.info("Formatting comparison response...")

        if "error" in comparison_result:
            return f"⚠️ {comparison_result['error']}"

        cheapest = comparison_result["cheapest"]
        highest = comparison_result["highest"]
        diff = comparison_result["price_difference"]

        response = f"""
🛒 **Price Comparison Result**

✅ Cheapest Option:
{cheapest['source']} — {cheapest['title']}
Price: ₹{cheapest['price']}
Link: {cheapest['url']}

💰 Highest Price:
{highest['source']} — {highest['title']}
Price: ₹{highest['price']}

📊 Price Difference: ₹{diff}
"""

        logger.info("Response formatting completed")

        return response.strip()

    def generate_llm_response(self, prompt: str) -> str:
        """
        Generate LLM-based response (optional)

        :param prompt: Input prompt
        :return: LLM output
        """

        if not self.llm:
            logger.warning("LLM not configured")
            return "LLM not configured."

        logger.info("Generating LLM response...")

        return self.llm.invoke(prompt)
