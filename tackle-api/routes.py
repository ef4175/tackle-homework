from typing import Dict, List, Optional, Union

from flask import jsonify
from flask.wrappers import Response

from config import app
from models import Product, Vendor


# Note: Don't expose auto-increment primary keys in REST APIs.
# UUIDs are more secure.

@app.route('/vendors', methods={'GET'})
def get_vendors() -> Response:
    vendors: List[Vendor] = Vendor.query.all()
    vendors_by_id_asc: List[Vendor] = sorted(vendors, key=lambda v: v.id)
    serialized_vendors: List[Dict[str, Union[int, str]]] = [
        dict(vendor) for vendor in vendors_by_id_asc
    ]
    res: Response = jsonify(serialized_vendors)
    return res

@app.route('/vendors/<vendor_id>/products', methods={'GET'})
def get_products(vendor_id: str) -> Response:
    casted_id: int = int(vendor_id)
    queried_vendor: Optional[Vendor] = (
        Vendor.query.filter_by(id=casted_id).first()
    )
    if queried_vendor is None:
        msg: Dict[str, str] = {'message': 'Vendor not found.'}
        not_found_res: Response = jsonify(msg), 404
        return not_found_res
    products: List[Product] = queried_vendor.products
    products_by_id_asc: List[Product] = sorted(products, key=lambda p: p.id)
    serialized_products: List[Dict[str, Union[int, str]]] = [
        dict(product) for product in products_by_id_asc
    ]
    res: Response = jsonify(serialized_products)
    return res

@app.route(
    '/vendors/<vendor_id>/products/<product_id>/orders',
    methods={'GET'},
)
def get_orders(vendor_id: str, product_id: str) -> Response:
    casted_vendor_id: int = int(vendor_id)
    queried_vendor: Optional[Vendor] = (
        Vendor.query.filter_by(id=casted_vendor_id).first()
    )
    if queried_vendor is None:
        msg: Dict[str, str] = {'message': 'Vendor not found.'}
        not_found_res: Response = jsonify(msg), 404
        return not_found_res
    casted_product_id: int = int(product_id)
    queried_product: Optional[Product] = (
        Product.query.filter_by(
            vendor_id=casted_vendor_id,
            id=casted_product_id,
        ).first()
    )
    if queried_product is None:
        msg: Dict[str, str] = {'message': 'Product not found.'}
        not_found_res: Response = jsonify(msg), 404
        return not_found_res
    orders: List[Order] = queried_product.orders
    orders_by_id_asc: List[Order] = sorted(orders, key=lambda o: o.id)
    serialized_orders: List[Dict[str, Union[int, str]]] = [
        dict(order) for order in orders_by_id_asc
    ]
    res: Response = jsonify(serialized_orders)
    return res
