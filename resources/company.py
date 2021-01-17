"""
Company Resource Module

This module contains only companies resource methods.
"""

from flask_restful import Resource, reqparse
from models.company import Model, CompanyModel
from resources.resource import Resource as ResourceHelper, non_empty_string
from flask_jwt_extended import jwt_required

parser = reqparse.RequestParser()
parser.add_argument('name', type=non_empty_string, required=True, help="Required field")
parser.add_argument('position', type=non_empty_string, required=True, help="Required field")
parser.add_argument('assignments', type=non_empty_string, required=True, help="Required field")
parser.add_argument('started_at', type=non_empty_string, required=True, help="Required field")
parser.add_argument('ended_at')
parser.add_argument('segment_id', type=non_empty_string, required=True, help="Required field")


class Company(Resource, ResourceHelper):
    """
    Company Resource Class

    This class contains only Company resource methods.
    """

    def __init__(self, model: Model = CompanyModel) -> None:
        """
        Company Resource Constructor

        Loads the CompanyModel passed as param.
        """
        super().__init__(model)

    def get(self, _id: int) -> dict:
        """
        Accesses Company.find_by_id() and returns the serached company by id.
        """
        return self.find_by_id(_id)

    @jwt_required
    def put(self, _id: int) -> tuple:
        """
        Accesses Company.update() to update the company found by passed id and returns a list of saved companies.
        """
        data = parser.parse_args()

        return self.update(_id, data)

    @jwt_required
    def delete(self, _id: int) -> tuple:
        """
        Accesses Company.destroy() to delete the company found by passed id and returns a list of saved company.
        """
        return self.destroy(_id)


class CompanyList(Resource, ResourceHelper):
    """
    CompanyList Resource Class

    This class contains only CompanyList resource methods.
    """

    def __init__(self, model: Model = CompanyModel) -> None:
        """
        CompanyList Resource Constructor

        Loads the CompanyModel passed as param.
        """
        super().__init__(model)

    def get(self) -> tuple:
        """
        Accesses CompanyList.get_all() and returns companys list.
        """
        return self.get_all()

    @jwt_required
    def post(self) -> tuple:
        """
        Accesses CompanyList.store() to insert the company load by passed data and returns a list of saved companies.
        """
        data = parser.parse_args()

        return self.store(data)
