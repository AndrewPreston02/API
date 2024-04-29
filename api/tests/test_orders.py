from fastapi.testclient import TestClient
from ..controllers import orders as controller
from ..main import app
import pytest
from ..models import orders as model

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_order(db_session):
    # Create a sample order
    order_data = {
        "customer_id": 1,
        "order_status": "Processing",
        "tracking_number": 123456789,
        "total_price": 7.00,
        "description": "Test order",
        "promotion_id": None
    }

    order_object = model.Order(**order_data)

    # Call the create function
    created_order = controller.create(db_session, order_object)

    # Assertions
    assert created_order is not None
    assert created_order.customer_id == 1
    assert created_order.order_status == "Processing"
    assert created_order.tracking_number == 123456789
    assert created_order.total_price == 7.00
    assert created_order.description == "Test order"
    assert created_order.promotion_id is None
