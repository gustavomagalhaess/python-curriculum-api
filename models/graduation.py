from database.db import db
from models.model import Model, datetime, string_to_date

class GraduationModel(db.Model, Model):
    __tablename__ = 'graduations'

    id          = db.Column(db.Integer, primary_key = True)
    course      = db.Column(db.String(50), nullable = False, unique = True)
    institution = db.Column(db.String(100), nullable = False, unique = True)
    started_at  = db.Column(db.Date(), nullable = False, default = datetime.date.today(), unique = True)
    ended_at    = db.Column(db.Date())
    segment_id  = db.Column(db.Integer, db.ForeignKey('segments.id'), nullable = False, default = 1)
    segment     = db.relationship('SegmentModel')

    def __init__(self, course, institution, started_at, segment_id, ended_at = None, _id = None):
        self.id          = _id
        self.course      = course
        self.institution = institution
        self.started_at  = string_to_date(started_at)
        self.ended_at    = string_to_date(ended_at) if ended_at else None
        self.segment_id  = segment_id

    def json(self):
        return {
            'id': self.id,
            'course': self.course,
            'institution': self.institution,
            'started_at': self.started_at.isoformat(),
            'ended_at': self.ended_at.isoformat() if self.ended_at else None,
            'segment': {'id': self.segment.id, 'name': self.segment.name}
        }