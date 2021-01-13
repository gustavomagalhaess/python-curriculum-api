from database.db import db
from models.model import Model, datetime, string_to_date

class CertificationModel(db.Model, Model):
    __tablename__ = 'certifications'

    id           = db.Column(db.Integer, primary_key = True)
    name         = db.Column(db.String(100), nullable = False, unique = True)
    organization = db.Column(db.String(100), nullable = False, unique = True)
    issued_at    = db.Column(db.Date(), nullable = False, default = datetime.date.today(), unique = True)
    expires_at   = db.Column(db.Date())
    segment_id   = db.Column(db.Integer, db.ForeignKey('segments.id'), nullable = False, default = 1)
    segment      = db.relationship('SegmentModel')

    def __init__(self, name: str, organization: str, issued_at: datetime, segment_id: int, expires_at: datetime = None, _id: int = None) -> None:
        self.id           = _id
        self.name         = name
        self.organization = organization
        self.issued_at    = string_to_date(issued_at)
        self.expires_at   = string_to_date(expires_at) if expires_at else None
        self.segment_id   = segment_id

    def json(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'organization': self.organization,
            'issued_at': self.issued_at.isoformat(),
            'expires_at': self.expires_at.isoformat() if self.expires_at else None,
            'segment': {'id': self.segment.id, 'name': self.segment.name}
        }

    def curriculum_json(self) -> dict:
        return {'id': self.id, 'name': self.name}