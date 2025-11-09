from sales_api import fetch_recent_orders

def test_api_returns_data():
    data = fetch_recent_orders()
    assert isinstance(data, list)
