'''
Graduation Resource Module

This module contains only graduation resource methods.
'''

from flask_restful import Resource, reqparse
from models.graduation import Model, GraduationModel
from resources.resource import Resource as ResourceHelper, non_empty_string
from flask_jwt_extended import jwt_required

parser = reqparse.RequestParser()
parser.add_argument('course', type=non_empty_string, required=True, help="Required field")
parser.add_argument('institution', type=non_empty_string, required=True, help="Required field")
parser.add_argument('started_at', type=non_empty_string, required=True, help="Required field")
parser.add_argument('ended_at')
parser.add_argument('segment_id', type=non_empty_string, required=True, help="Required field")

class Graduation(Resource, ResourceHelper):
    '''
    Graduation Resource Class

    This class contains only Graduation resource methods.
    '''
    def __init__(self, model: Model = GraduationModel) -> None:
        '''
        Graduation Resource Constructor

        Loads the GraduationModel passed as param.
        '''
        super().__init__(model)
    
    def get(self, _id: int) -> dict:
        '''
        Accesses Graduation.find_by_id() and returns the serached graduation by id.
        '''
        return self.find_by_id(_id)
    
    @jwt_required
    def put(self, _id: int) -> list:
        '''
        Accesses Graduation.update() to update the graduation found by passed id and returns a list of saved graduations.
        '''
        data = parser.parse_args()

        return self.update(_id, data)

    @jwt_required
    def delete(self, _id: int) -> list:
        '''
        Accesses Graduation.delete() to delete the graduation found by passed id and returns a list of saved graduation.
        '''
        return self.destroy(_id)


class GraduationList(Resource, ResourceHelper):
    '''
    GraduationList Resource Class

    This class contains only GraduationList resource methods.
    '''
    def __init__(self, model: Model = GraduationModel) -> None:
        '''
        GraduationList Resource Constructor

        Loads the GraduationModel passed as param.
        '''
        super().__init__(model)

    def get(self) -> list:
        '''
        Accesses GraduationList.get_all() and returns graduations list.
        '''
        return self.get_all()

    @jwt_required
    def post(self) -> list:
        '''
        Accesses GraduationList.store() to insert the graduation load by passed data and returns a list of saved graduations.
        '''
        data = parser.parse_args()

        return self.store(data)