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

    def __init__(self, model: Model = ProductModel) -> None:
        super().__init__(model)
    
    def get(self, _id: int) -> dict:
        return self.find_by_id(_id)
    
    @jwt_required
    def put(self, _id: int) -> list:
        data = parser.parse_args()

        return self.update(_id, data)

    @jwt_required
    def delete(self, _id: int) -> list:
        return self.destroy(_id)


class ProductList(Resource, ResourceHelper):
    
    def __init__(self, model: Model = ProductModel) -> None:
        super().__init__(model)

    def get(self) -> list:
        return self.get_all()

    @jwt_required
    def post(self) -> list:
        data = parser.parse_args()

        return self.store(data)