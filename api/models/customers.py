from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from ..dependencies.database import Base

class Customer(Base):
    tablename = "customers"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100))
    email = Column(String(100), unique=True, index=True)
    phone_number = Column(String(20))
    address = Column(String(300))