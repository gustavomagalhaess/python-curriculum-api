from database.db import db
from models.model import Model
import datetime

class ResumeModel(db.Model, Model):
    __tablename__ = 'resumes'

    id          = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.String(1000), nullable = False)
    created_at  = db.Column(db.Date(), nullable = False, default = datetime.date.today())
    segment_id  = db.Column(db.Integer, db.ForeignKey('segments.id'), nullable = False, default = 1)
    segment     = db.relationship('SegmentModel')

    def __init__(self, description, segment_id, _id = None):
        self.id          = _id
        self.description = description
        self.segment_id  = segment_id

    def json(self):
        return {
            'id': self.id, 
            'description': self.description, 
            'created_at': self.created_at.isoformat(), 
            'segment': {'id': self.segment.id, 'name': self.segment.name}
        }