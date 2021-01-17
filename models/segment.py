"""
SegmentModel Module

This module contains only SegmentModel methods.
"""

from database.db import db
from models.model import Model


class SegmentModel(db.Model, Model):
    """
    SegmentModel Class

    This class contains only SegmentModel methods and represents the segments table in database.
    """
    __tablename__ = 'segments'

    id          = db.Column(db.Integer(), primary_key=True)
    name        = db.Column(db.String(50), nullable=False, unique=True)
    description = db.Column(db.String(100), nullable=False)

    def __init__(self, name: str, description: str, _id: int = None) -> None:
        """
        Loads a SegmentModel.
        """
        self.id          = _id
        self.name        = name
        self.description = description

    def json(self) -> dict:
        """
        Retruns a SkillModel as a json format.
        """
        return {'id': self.id, 'name': self.name, 'description': self.description}
