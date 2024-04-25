from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class OrderBase(BaseModel):
    customer_id: int
    description: Optional[str] = None
    order_status: str
    total_price: float
    tracking_number: int


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    description: Optional[str] = None
    order_status: str


class Order(OrderBase):
    id: int
    order_date: Optional[datetime] = None

    class ConfigDict:
        from_attributes = True
