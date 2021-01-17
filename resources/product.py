"""
Product Resource Module

This module contains only products resource methods.
"""

from flask_restful import Resource, reqparse
from models.product import Model, ProductModel
from resources.resource import Resource as ResourceHelper, non_empty_string
from flask_jwt_extended import jwt_required

parser = reqparse.RequestParser()
parser.add_argument('name', type=non_empty_string, required=True, help="Required field")
parser.add_argument('description', type=non_empty_string, required=True, help="Required field")
parser.add_argument('created_at', type=non_empty_string, required=True, help="Required field")
parser.add_argument('url', type=non_empty_string, required=True, help="Required field")
parser.add_argument('segment_id', type=non_empty_string, required=True, help="Required field")
parser.add_argument('company_id', type=non_empty_string, required=True, help="Required field")

class Product(Resource, ResourceHelper):
    """
    Product Resource Class

    This class contains only Product resource methods.
    """
    def __init__(self, model: Model = ProductModel) -> None:
        """
        Product Resource Constructor

        Loads the ProductModel passed as param.
        """
        super().__init__(model)
    
    def get(self, _id: int) -> dict:
        """
        Accesses Product.find_by_id() and returns the serached product by id.
        """
        return self.find_by_id(_id)
    
    @jwt_required
    def put(self, _id: int) -> list:
        """
        Accesses Product.update() to update the product found by passed id and returns a list of saved products.
        """
        data = parser.parse_args()

        return self.update(_id, data)

    @jwt_required
    def delete(self, _id: int) -> list:
        """
        Accesses Product.destroy() to delete the product found by passed id and returns a list of saved products.
        """
        return self.destroy(_id)


class ProductList(Resource, ResourceHelper):
    """
    ProductList Resource Class

    This class contains only ProductList resource methods.
    """
    def __init__(self, model: Model = ProductModel) -> None:
        """
        ProductList Resource Constructor

        Loads the ProductModel passed as param.
        """
        super().__init__(model)

    def get(self) -> list:
        """
        Accesses ProductList.get_all() and returns products list.
        """
        return self.get_all()

    @jwt_required
    def post(self) -> list:
        """
        Accesses ProductList.store() to insert the product load by passed data and returns a list of saved products.
        """
        data = parser.parse_args()

        return self.store(data)