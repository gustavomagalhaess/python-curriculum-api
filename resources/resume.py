'''
Resume Resource Module

This module contains only resumes resource methods.
'''

from flask_restful import Resource, reqparse
from models.resume import Model, ResumeModel
from resources.resource import Resource as ResourceHelper, non_empty_string
from flask_jwt_extended import jwt_required

parser = reqparse.RequestParser()
parser.add_argument('description', type=non_empty_string, required=True, help="Required field")
parser.add_argument('segment_id', type=non_empty_string, required=True, help="Required field")

class Resume(Resource, ResourceHelper):
    '''
    Resume Resource Class

    This class contains only Resume resource methods.
    '''
    def __init__(self, model: Model = ResumeModel) -> None:
        '''
        Resume Resource Constructor

        Loads the ResumeModel passed as param.
        '''
        super().__init__(model)
    
    def get(self, _id: int) -> dict:
        '''
        Accesses Resume.find_by_id() and returns the serached resume by id.
        '''
        return self.find_by_id(_id)
    
    @jwt_required
    def put(self, _id: int) -> list:
        '''
        Accesses Resume.update() to update the resume found by passed id and returns a list of saved resumes.
        '''
        data = parser.parse_args()

        return self.update(_id, data)

    @jwt_required
    def delete(self, _id: int) -> list:
        '''
        Accesses Resume.destroy() to delete the resume found by passed id and returns a list of saved resume.
        '''
        return self.destroy(_id)


class ResumeList(Resource, ResourceHelper):
    '''
    ResumeList Resource Class

    This class contains only ResumeList resource methods.
    '''
    def __init__(self, model: Model = ResumeModel) -> None:
        '''
        ResumeList Resource Constructor

        Loads the ResumeModel passed as param.
        '''
        super().__init__(model)

    def get(self) -> list:
        '''
        Accesses ResumeList.get_all() and returns resume list.
        '''
        return self.get_all()

    @jwt_required
    def post(self) -> list:
        '''
        Accesses ResumeList.store() to insert the resume load by passed data and returns a list of saved resumes.
        '''
        data = parser.parse_args()

        return self.store(data)