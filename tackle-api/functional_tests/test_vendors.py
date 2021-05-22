from flask.wrappers import Response

from typing import Dict, List, Union

from routes import app
from util import build_or_refresh_db


build_or_refresh_db()

def test_get_vendors_success() -> None:
    with app.test_client() as client:
        res: Response = client.get('/vendors')
        payload: List[Dict[str, Union[int, str]]] = res.get_json()
        expected: List[Dict[str, Union[int, str]]] = [
            {
                'id': 1,
                'name': 'Tackle.io',
            },
        ]
        assert res.status_code == 200
        assert payload == expected
