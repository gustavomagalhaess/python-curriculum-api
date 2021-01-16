'''
Presentation Resource Module

This module contains only presentations resource methods.
'''

from flask_restful import Resource, reqparse
from models.presentation import Model, PresentationModel
from resources.resource import Resource as ResourceHelper, non_empty_string
from flask_jwt_extended import jwt_required

parser = reqparse.RequestParser()
parser.add_argument('name', type=non_empty_string, required=True, help="Required field")
parser.add_argument('performed_at', type=non_empty_string, required=True, help="Required field")
parser.add_argument('city', type=non_empty_string, required=True, help="Required field")
parser.add_argument('state')
parser.add_argument('country', type=non_empty_string, required=True, help="Required field")
parser.add_argument('segment_id', type=non_empty_string, required=True, help="Required field")
parser.add_argument('company_id', type=non_empty_string, required=True, help="Required field")

class Presentation(Resource, ResourceHelper):
    '''
    Presentation Resource Class

    This class contains only Presentation resource methods.
    '''
    def __init__(self, model: Model = PresentationModel) -> None:
        '''
        Presentation Resource Constructor

        Loads the PresentationModel passed as param.
        '''
        super().__init__(model)
    
    def get(self, _id: int) -> dict:
        '''
        Accesses Presentation.find_by_id() and returns the serached presentation by id.
        '''
        return self.find_by_id(_id)
    
    @jwt_required
    def put(self, _id: int) -> list:
        '''
        Accesses Presentation.update() to update the presentation found by passed id and returns a list of saved presentations.
        '''
        data = parser.parse_args()

        return self.update(_id, data)

    @jwt_required
    def delete(self, _id: int) -> list:
        '''
        Accesses Presentation.destroy() to delete the presentation found by passed id and returns a list of saved presentation.
        '''
        return self.destroy(_id)


class PresentationList(Resource, ResourceHelper):
    '''
    PresentationList Resource Class

    This class contains only PresentationList resource methods.
    '''
    def __init__(self, model: Model = PresentationModel) -> None:
        '''
        PresentationList Resource Constructor

        Loads the PresentationModel passed as param.
        '''
        super().__init__(model)

    def get(self) -> list:
        '''
        Accesses PresentationList.get_all() and returns presentations list.
        '''
        return self.get_all()

    @jwt_required
    def post(self) -> list:
        '''
        Accesses PresentationList.store() to insert the presentation load by passed data and returns a list of saved presentation.
        '''
        data = parser.parse_args()

        return self.store(data)