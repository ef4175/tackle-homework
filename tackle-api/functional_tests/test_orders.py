from datetime import datetime
from dateutil.relativedelta import relativedelta
from typing import Dict, List, Union

from flask.wrappers import Response

from routes import app
from util import build_or_refresh_db


build_or_refresh_db()

def test_get_orders_where_vendor_doesnt_exist() -> None:
    with app.test_client() as client:
        res: Response = client.get('vendors/555/products/1/orders')
        payload: Dict[str, str] = res.get_json()
        expected: Dict[str, str] = {'message': 'Vendor not found.'}
        assert res.status_code == 404
        assert payload == expected

def test_get_orders_where_product_doesnt_exist() -> None:
    with app.test_client() as client:
        res: Response = client.get('vendors/1/products/176/orders')
        payload: Dict[str, str] = res.get_json()
        expected: Dict[str, str] = {'message': 'Product not found.'}
        assert res.status_code == 404
        assert payload == expected

def test_get_orders_success() -> None:
    with app.test_client() as client:
        res: Response = client.get('/vendors/1/products/1/orders')
        payload: List[Dict[str, Union[int, str]]] = res.get_json()
        now: datetime = datetime.now()
        dt_fmt: str = '%Y-%m-%d'
        expected: List[Dict[str, Union[int, str]]] = [
            {
                'id': 1,
                'fullName': 'Linus Torvalds',
                'orderDate': (now - relativedelta(months=1)).strftime(dt_fmt),
            },
            {
                'id': 2,
                'fullName': 'Elon Musk',
                'orderDate': (now - relativedelta(months=1)).strftime(dt_fmt),
            },
            {
                'id': 3,
                'fullName': 'Alan Turing',
                'orderDate': (now - relativedelta(months=4)).strftime(dt_fmt),
            },
            {
                'id': 4,
                'fullName': 'Katherine Johnson',
                'orderDate': (now - relativedelta(months=4)).strftime(dt_fmt),
            },
        ]
        assert res.status_code == 200
        assert payload == expected

