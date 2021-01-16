'''
Segment Resource Module

This module contains only segments resource methods.
'''

from flask_restful import Resource, reqparse
from models.segment import Model, SegmentModel
from resources.resource import Resource as ResourceHelper, non_empty_string
from flask_jwt_extended import jwt_required

parser = reqparse.RequestParser()
parser.add_argument('name', type=non_empty_string, required=True, help="Required field")
parser.add_argument('description', type=non_empty_string, required=True, help="Required field")

class Segment(Resource, ResourceHelper):
    '''
    Segment Resource Class

    This class contains only Segment resource methods.
    '''
    def __init__(self, model: Model = SegmentModel) -> None:
        '''
        Segment Resource Constructor

        Loads the SegmentModel passed as param.
        '''
        super().__init__(model)
    
    def get(self, _id: int) -> dict:
        '''
        Accesses Segment.find_by_id() and returns the serached segment by id.
        '''
        return self.find_by_id(_id)
    
    @jwt_required
    def put(self, _id: int) -> list:
        '''
        Accesses Segment.update() to update the segment found by passed id and returns a list of saved segments.
        '''
        data = parser.parse_args()

        return self.update(_id, data)

    @jwt_required
    def delete(self, _id: int) -> list:
        '''
        Accesses Segment.destroy() to delete the segment found by passed id and returns a list of saved segments.
        '''
        return self.destroy(_id)


class SegmentList(Resource, ResourceHelper):
    '''
    SegmentList Resource Class

    This class contains only SegmentList resource methods.
    '''
    def __init__(self, model: Model = SegmentModel) -> None:
        '''
        SegmentList Resource Constructor

        Loads the SegmentModel passed as param.
        '''
        super().__init__(model)

    def get(self) -> list:
        '''
        Accesses SegmentList.get_all() and returns segments list.
        '''
        return self.get_all()

    @jwt_required
    def post(self) -> list:
        '''
        Accesses SegmentList.store() to insert the segment load by passed data and returns a list of saved segments.
        '''
        data = parser.parse_args()

        return self.store(data)