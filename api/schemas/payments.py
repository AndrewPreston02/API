from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel


class PaymentBase(BaseModel):
    order_id: int
    card_information: str
    transaction_status: str
    payment_type: str


class PaymentCreate(PaymentBase):
    pass


class PaymentUpdate(BaseModel):
    card_information: Optional[str] = None
    transaction_status: Optional[str] = None
    payment_type: Optional[str] = None


class Payment(PaymentBase):
    id: int

    class Config:
        orm_mode = True
