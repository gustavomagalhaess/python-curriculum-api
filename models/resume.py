'''
ResumeModel Module

This module contains only ResumeModel methods.
'''

from database.db import db
from models.model import Model
import datetime

class ResumeModel(db.Model, Model):
    '''
    ResumeModel Class

    This class contains only ResumeModel methods and represents the resumes table in database.
    '''
    __tablename__ = 'resumes'

    id          = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.String(1000), nullable = False)
    created_at  = db.Column(db.Date(), nullable = False, default = datetime.date.today())
    segment_id  = db.Column(db.Integer, db.ForeignKey('segments.id'), nullable = False, default = 1)
    segment     = db.relationship('SegmentModel')

    def __init__(self, description: str, segment_id: int, _id: int = None) -> None:
        '''
        Loads a ResumeModel.
        '''
        self.id          = _id
        self.description = description
        self.segment_id  = segment_id

    def json(self) -> dict:
        '''
        Retruns a ResumeModel as a json format.
        '''
        return {
            'id': self.id, 
            'description': self.description, 
            'created_at': self.created_at.isoformat(), 
            'segment': {'id': self.segment.id, 'name': self.segment.name}
        }