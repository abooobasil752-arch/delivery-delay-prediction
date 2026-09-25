"""Pydantic schemas for API."""

from pydantic import BaseModel
from typing import Optional

class OrderData(BaseModel):
    """Order data for prediction."""
    order_id: str
    customer_id: str
    item_count: int
    delivery_distance: float
    order_value: float
    day_of_week: int
    hour_of_day: int
    is_weekend: int
    courier_experience: float

class PredictionResponse(BaseModel):
    """Prediction response."""
    order_id: str
    prediction: int
    probability: float
    model_version: str

class HealthResponse(BaseModel):
    """Health check response."""
    status: str
    version: str

class InfoResponse(BaseModel):
    """Model info response."""
    model_name: str
    model_type: str
    model_version: str
