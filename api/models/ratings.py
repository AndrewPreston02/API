from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Rating(Base):
    tablename = "ratings"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customer.id"))
    order_id = Column(Integer, ForeignKey("orders.id"))
    rating = Column(Integer, index=True, nullable=False)
    comment = Column(String(500), unique=True, nullable=False)
    timestamp = Column(DATETIME, nullable=False, server_default=str(datetime.now()))

    customer = relationship("Customer", back_populates="ratings")
    order = relationship("Order", back_populates="ratings")