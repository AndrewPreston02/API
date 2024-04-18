from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Order(Base):
    tablename = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_name = Column(String(100), ForeignKey("customers.name"))
    order_date = Column(DATETIME, nullable=False, server_default=str(datetime.now()))
    tracking_number = Column(Integer, index=True, nullable=False)
    order_status = Column(String(100))
    total_price = Column(DECIMAL(4, 2), nullable=False, server_default='0.0')
    description = Column(String(300))