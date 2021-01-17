"""
ProductModel Module

This module contains only ProductModel methods.
"""

from database.db import db
from models.model import Model, datetime, string_to_date

class ProductModel(db.Model, Model):
    """
    ProductModel Class

    This class contains only ProductModel methods and represents the products table in database.
    """
    __tablename__ = 'products'

    id          = db.Column(db.Integer, primary_key = True)
    name        = db.Column(db.String(100), nullable = False, unique = True)
    description = db.Column(db.String(1000), nullable = False)
    created_at  = db.Column(db.Date(), nullable = False, default = datetime.date.today())
    url         = db.Column(db.String(250))
    segment_id  = db.Column(db.Integer, db.ForeignKey('segments.id'), nullable = False, default = 1)
    segment     = db.relationship('SegmentModel')
    company_id  = db.Column(db.Integer, db.ForeignKey('companies.id'))
    company     = db.relationship('CompanyModel')

    def __init__(self, name: str, description: str, created_at: datetime, segment_id: int, url: str = None, company_id: int = None, _id: int = None) -> None:
        """
        Loads a ProductModel.
        """
        self.id          = _id
        self.name        = name
        self.description = description
        self.created_at  = string_to_date(created_at)
        self.url         = url if url else None
        self.segment_id  = segment_id
        self.company_id  = company_id

    def json(self) -> dict:
        """
        Retruns a ProductModel as a json format.
        """
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'created_at': self.created_at.isoformat(),
            'url': self.url if self.url else None,
            'segment': {'id': self.segment.id, 'name': self.segment.name},
            'company': {'id': self.company.id, 'name': self.company.name} if self.company else None
        }
    
    def curriculum_json(self) -> dict:
        """
        Retruns a reduced ProductModel as a json format.
        """
        return {'id': self.id, 'name': self.name}