from flask_restful import Resource, reqparse
from models.certification import CertificationModel
from resources.resource import Resource as ResourceHelper, non_empty_string
from flask_jwt_extended import jwt_required

parser = reqparse.RequestParser()
parser.add_argument('name', type=non_empty_string, required=True, help="Required field")
parser.add_argument('organization', type=non_empty_string, required=True, help="Required field")
parser.add_argument('issued_at', type=non_empty_string, required=True, help="Required field")
parser.add_argument('expires_at')
parser.add_argument('segment_id', type=non_empty_string, required=True, help="Required field")

class Certification(Resource, ResourceHelper):
    
    def __init__(self, model = CertificationModel):
        super().__init__(model)
    
    def get(self, _id):
        return self.find_by_id(_id)
    
    @jwt_required
    def put(self, _id):
        data = parser.parse_args()

        return self.update(_id, data)

    @jwt_required
    def delete(self, _id):
        return self.destroy(_id)


class CertificationList(Resource, ResourceHelper):
        
    def __init__(self, model = CertificationModel):
        super().__init__(model)

    def get(self):
        return self.get_all()

    @jwt_required
    def post(self):
        data = parser.parse_args()

        return self.store(data)