from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    card_information = Column(String(100), nullable=False)
    transaction_status = Column(String(50), nullable=False)
    payment_type = Column(String(50), nullable=False)
    order_id = Column(Integer, ForeignKey("orders.id"))

    order = relationship("Order", back_populates="payments")
