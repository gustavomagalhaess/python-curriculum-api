from database.db import db
from models.model import Model, datetime, string_to_date

class PresentationModel(db.Model, Model):
    __tablename__ = 'presentations'

    id           = db.Column(db.Integer, primary_key = True)
    name         = db.Column(db.String(100), nullable = False, unique = True)
    performed_at = db.Column(db.Date(), nullable = False, default = datetime.date.today())
    city         = db.Column(db.String(250), nullable = False)
    state        = db.Column(db.String(250))
    country      = db.Column(db.String(250), nullable = False)
    segment_id   = db.Column(db.Integer, db.ForeignKey('segments.id'), nullable = False, default = 1)
    segment      = db.relationship('SegmentModel')
    company_id   = db.Column(db.Integer, db.ForeignKey('companies.id'))
    company      = db.relationship('CompanyModel')

    def __init__(self, name, performed_at, city, country, segment_id, state = None, company_id = None, _id = None):
        self.id           = _id
        self.name         = name
        self.performed_at = string_to_date(performed_at)
        self.city         = city
        self.state        = state if state else None
        self.country      = country
        self.segment_id   = segment_id
        self.company_id   = company_id

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'performed_at': self.performed_at.isoformat(),
            'city': self.city,
            'state': self.state if self.state else None,
            'country': self.country,
            'segment': {'id': self.segment.id, 'name': self.segment.name},
            'company': {'id': self.company.id, 'name': self.company.name} if self.company else None
        }

    def curriculum_json(self):
        return {'id': self.id, 'name': self.name, 'performed_at': self.performed_at.isoformat()}