'''
Certification Resource Module

This module contains only certifications resource methods.
'''

from flask_restful import Resource, reqparse
from models.certification import Model, CertificationModel
from resources.resource import Resource as ResourceHelper, non_empty_string
from flask_jwt_extended import jwt_required

parser = reqparse.RequestParser()
parser.add_argument('name', type=non_empty_string, required=True, help="Required field")
parser.add_argument('organization', type=non_empty_string, required=True, help="Required field")
parser.add_argument('issued_at', type=non_empty_string, required=True, help="Required field")
parser.add_argument('expires_at')
parser.add_argument('segment_id', type=non_empty_string, required=True, help="Required field")

class Certification(Resource, ResourceHelper):
    '''
    Certification Resource Class

    This class contains only Certification resource methods.
    '''
    def __init__(self, model: Model = CertificationModel) -> None:
        '''
        Certification Resource Constructor

        Loads the CertificationModel passed as param.
        '''
        super().__init__(model)
    
    def get(self, _id: int) -> dict:
        '''
        Accesses Certification.find_by_id() and returns the serached certification by id.
        '''
        return self.find_by_id(_id)
    
    @jwt_required
    def put(self, _id: int) -> list:
        '''
        Accesses Certification.update() to update the certification found by passed id and returns a list of saved certifications.
        '''
        data = parser.parse_args()

        return self.update(_id, data)

    @jwt_required
    def delete(self, _id: int) -> list:
        '''
        Accesses Certification.destroy() to delete the certification found by passed id and returns a list of saved certification.
        '''
        return self.destroy(_id)


class CertificationList(Resource, ResourceHelper):
    '''
    CertificationList Resource Class

    This class contains only CertificationList resource methods.
    '''   
    def __init__(self, model: Model = CertificationModel) -> None:
        '''
        CertificationList Resource Constructor

        Loads the CertificationModel passed as param.
        '''
        super().__init__(model)

    def get(self) -> list:
        '''
        Accesses CertificationList.get_all() and returns certifications list.
        '''
        return self.get_all()

    @jwt_required
    def post(self) -> list:
        '''
        Accesses CertificationList.store() to insert the certification load by passed data and returns a list of saved certifications.
        '''
        data = parser.parse_args()

        return self.store(data)