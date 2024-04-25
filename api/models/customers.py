from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship

from ..dependencies.database import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), index=True)
    email = Column(String(100), unique=True, index=True)
    phone_number = Column(String(20))
    address = Column(String(300))

    orders = relationship("Order", back_populates="customer")
    ratings = relationship("Rating", back_populates="customer")
