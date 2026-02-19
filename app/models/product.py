"""
Product Model

Defines the standard structure for product data
across all platforms (Amazon, Flipkart, Shopify, etc.)
"""

from pydantic import BaseModel, Field
from typing import Optional


class Product(BaseModel):
    source: str = Field(..., description="Platform source (Amazon, Flipkart, etc.)")
    title: str = Field(..., description="Product title/name")
    price: float = Field(..., description="Product price")
    currency: str = Field(default="INR", description="Currency code")
    url: str = Field(..., description="Product URL")
    availability: Optional[str] = Field(default="Unknown", description="Stock status")

    class Config:
        json_schema_extra = {
            "example": {
                "source": "Flipkart",
                "title": "iPhone 15 (128GB)",
                "price": 69999.0,
                "currency": "INR",
                "url": "https://flipkart.com/iphone15",
                "availability": "In Stock"
            }
        }
