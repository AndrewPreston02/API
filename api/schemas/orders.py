from datetime import datetime
from typing import Optional
from pydantic import BaseModel



class OrderBase(BaseModel):
    customer_name: str
    description: Optional[str] = None
    order_status: str


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    customer_name: Optional[str] = None
    description: Optional[str] = None
    order_status: str


class Order(OrderBase):
    id: int
    order_date: Optional[datetime] = None
    description: Optional[str] = None

    class ConfigDict:
        from_attributes = True