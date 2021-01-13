from __future__ import annotations
from database.db import db, IntegrityError, SQLAlchemyError
import datetime

def string_to_date(string_date: str) -> datetime:
    Y, m, d = [int(item) for item in string_date.split('-')]

    return datetime.datetime(Y, m, d)

class DataBaseException(SQLAlchemyError):
    def __init__(self, message: str) -> None:
        self.message = message


class Model():
    @classmethod
    def get_all(cls) -> list:
        return cls.query.order_by(cls.id.desc()).all()

    @classmethod
    def find_by_id(cls, _id: int) -> Model:
        return cls.query.filter_by(id = _id).first()
    
    @classmethod
    def get_all_by_segment(cls, segment_id: int, order_by_date: bool = False) -> list:
        if not order_by_date:
            rows = cls.query.filter_by(segment_id = segment_id).order_by(cls.id.desc()).all()
        elif hasattr(cls, 'started_at'):
            rows = cls.query.filter_by(segment_id = segment_id).order_by(cls.started_at.desc()).all()
        else:
            rows = cls.query.filter_by(segment_id = segment_id).order_by(cls.performed_at.desc()).all()
        
        return rows
    
    @classmethod
    def get_current_by_segment(cls, segment_id: int) -> Model:
        return cls.query.filter_by(segment_id = segment_id).order_by(cls.id.desc()).first()

    def save(self) -> None:
        try:
            db.session.add(self)
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            raise DataBaseException('There already is this item saved.')
        except SQLAlchemyError as e:
            db.session.rollback()
            raise DataBaseException('An error occurred saving the item.')

    def delete(self) -> None:
        try:
            db.session.delete(self)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            raise DataBaseException('An error occurred deleting the item.')