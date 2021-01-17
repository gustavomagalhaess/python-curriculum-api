"""
Skill Resource Module

This module contains only skills resource methods.
"""

from flask_restful import Resource, reqparse
from models.skill import Model, SkillModel
from resources.resource import Resource as ResourceHelper, non_empty_string
from flask_jwt_extended import jwt_required

parser = reqparse.RequestParser()
parser.add_argument('name', type=non_empty_string, required=True, help="Required field")
parser.add_argument('description', type=non_empty_string, required=True, help="Required field")
parser.add_argument('level', type=non_empty_string, required=True, help="Required field")
parser.add_argument('segment_id', type=non_empty_string, required=True, help="Required field")


class Skill(Resource, ResourceHelper):
    """
    Skill Resource Class

    This class contains only Skill resource methods.
    """

    def __init__(self, model: Model = SkillModel) -> None:
        """
        Skill Resource Constructor

        Loads the SkillModel passed as param.
        """
        super().__init__(model)

    def get(self, _id: int) -> tuple:
        """
        Accesses Skill.find_by_id() and returns the serached skill by id.
        """
        return self.find_by_id(_id)

    @jwt_required
    def put(self, _id: int) -> tuple:
        """
        Accesses Skill.update() to update the skill found by passed id and returns a list of saved skills.
        """
        data = parser.parse_args()

        return self.update(_id, data)

    @jwt_required
    def delete(self, _id: int) -> tuple:
        """
        Accesses Skill.destroy() to delete the skill found by passed id and returns a list of saved skill.
        """
        return self.destroy(_id)


class SkillList(Resource, ResourceHelper):
    """
    SkillList Resource Class

    This class contains only SkillList resource methods.
    """

    def __init__(self, model: Model = SkillModel) -> None:
        """
        SkillList Resource Constructor

        Loads the SkillModel passed as param.
        """
        super().__init__(model)

    def get(self) -> tuple:
        """
        Accesses SkillList.get_all() and returns skills list.
        """
        return self.get_all()

    @jwt_required
    def post(self) -> tuple:
        """
        Accesses SkillList.store() to insert the skill load by passed data and returns a list of saved skills.
        """
        data = parser.parse_args()

        return self.store(data)
