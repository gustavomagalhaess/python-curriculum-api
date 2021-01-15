'''
Model Module

This module contains common helper functions and methods in all application. It's supposed to 
include here any new shared function or methods.
'''

from __future__ import annotations
from database.db import db, IntegrityError, SQLAlchemyError
import datetime

def string_to_date(string_date: str) -> datetime:
    '''
    Converts the string_date string (YYYY-MM-DD) to datetime type.
    '''
    Y, m, d = [int(item) for item in string_date.split('-')]

    return datetime.datetime(Y, m, d)

class DataBaseException(SQLAlchemyError):
    '''
    DataBaseException class

    This class inherits from SQLAlchemyError class to be used as a Database Exception.
    '''
    def __init__(self, message: str) -> None:
        self.message = message


class Model():
    '''
    Model Class

    This class contains common helper methods in all application. It's supposed to include here 
    any new shared methods.
    '''
    @classmethod
    def get_all(cls) -> list:
        '''
        Returns a list of items there are saved in database.
        '''
        return cls.query.order_by(cls.id.desc()).all()

    @classmethod
    def find_by_id(cls, _id: int) -> Model:
        '''
        Returns the item found by id there is saved in database.
        '''
        return cls.query.filter_by(id = _id).first()
    
    @classmethod
    def get_all_by_segment(cls, segment_id: int, order_by_date: bool = False) -> list:
        '''
        Returns a list of items by segment_id there are saved in database.
        '''
        if not order_by_date:
            rows = cls.query.filter_by(segment_id = segment_id).order_by(cls.id.desc()).all()
        elif hasattr(cls, 'started_at'):
            rows = cls.query.filter_by(segment_id = segment_id).order_by(cls.started_at.desc()).all()
        else:
            rows = cls.query.filter_by(segment_id = segment_id).order_by(cls.performed_at.desc()).all()
        
        return rows
    
    @classmethod
    def get_current_by_segment(cls, segment_id: int) -> Model:
        '''
        Returns the item by segment_id there is saved in database.
        '''
        return cls.query.filter_by(segment_id = segment_id).order_by(cls.id.desc()).first()

    def save(self) -> None:
        '''
        Saves the item in database.
        '''
        try:
            db.session.add(self)
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            raise DataBaseException('There already is this saved item.')
        except SQLAlchemyError as e:
            db.session.rollback()
            raise DataBaseException('An error occurred saving this item.')

    def delete(self) -> None:
        '''
        Deletes the item from database.
        '''
        try:
            db.session.delete(self)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            raise DataBaseException('An error occurred deleting this item.')