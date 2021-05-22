from flask.wrappers import Response

from typing import Dict, List, Union

from routes import app
from util import build_or_refresh_db


build_or_refresh_db()

def test_get_products_where_vendor_doesnt_exist() -> None:
    with app.test_client() as client:
        res: Response = client.get('/vendors/999/products')
        payload: Dict[str, str] = res.get_json()
        expected: Dict[str, str] = {'message': 'Vendor not found.'}
        assert res.status_code == 404
        assert payload == expected

def test_get_products_success() -> None:
    with app.test_client() as client:
        res: Response = client.get('/vendors/1/products')
        payload: List[Dict[str, Union[int, str]]] = res.get_json()
        expected: List[Dict[str, Union[int, str]]] = [
            {
                'id': 1,
                'title': 'Tackle Amazon Machine Image',
                'listingType': 'ami',
                'price': 1000,
            },
            {
                'id': 2,
                'title': 'Tackle for GovCloud',
                'listingType': 'saas',
                'price': 5000,
            },
        ]
        assert res.status_code == 200
        assert payload == expected
