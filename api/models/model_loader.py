from . import  customers, menuItem, payments, promotions, ratings, resources
from ..dependencies.database import engine


def index():
    customers.Base.metadata.create_all(engine)
    menuItem.Base.metadata.create_all(engine)
    payments.Base.metadata.create_all(engine)
    promotions.Base.metadata.create_all(engine)
    resources.Base.metadata.create_all(engine)
    ratings.Base.metadata.create_all(engine)
