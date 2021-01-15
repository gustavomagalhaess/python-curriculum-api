'''
Resource Module

This module contains common helper functions and methods in all application. It's supposed to 
include here any new shared function or methods.
'''

from models.model import Model, DataBaseException, string_to_date
import datetime
from typing import Optional

def non_empty_string(field: str) -> Exception:
    '''
    Checks if the field passed is empty.
    '''
    if not field:
        raise ValueError('Field must not be empty')

    return field

def verify_date_field(field, data: str) -> str:
    '''
    Checks if the field passed is a datetime field and converts the content from string to datetime.
    '''
    if field in ['started_at', 'ended_at', 'created_at', 'performed_at', 'issued_at', 'expires_at']:
        content = string_to_date(data)
    else:
        content = data

    return content

def check_json(item: Model) -> Optional[Model]:
    '''
    Checks if the item passed is not None to return Model.json() properly.
    '''
    if item:
        return item.json()
    else:
        return None
    
def check_curriculum_json(item: Model) -> Optional[Model]:
    '''
    Checks if the item passed is not None to return Model.curriculum_json() properly.
    '''
    if item:
        return item.curriculum_json()
    else:
        return None

def list_map(collection: list) -> list:
    '''
    Returns a list of Model.json() from a collection.
    '''
    return list(map(lambda item: check_json(item), collection))

def list_map_curriculum(collection: list) -> list:
    '''
    Returns a list of Model.curriculum_json() from a collection.
    '''
    return list(map(lambda item: check_curriculum_json(item), collection))

class Resource():
    '''
    Resource Class

    This class contains common helper methods in all application. It's supposed to include here 
    any new shared methods.
    '''
    def __init__(self, model: Model) -> None:
        '''
        Resource Constructor

        Loads the model passed as param.
        '''
        self.model = model
    
    def get_all(self) -> dict:
        '''
        Accesses Model.get_all() and returns a items list.
        '''
        items = self.model.get_all()

        return {'items': list_map(items)}, 200
    
    def find_by_id(self, _id: int) -> dict:
        '''
        Accesses Model.find_by_id() and retuns the serached item by id.
        '''
        item = self.model.find_by_id(_id)
        if item:
            return {'item': check_json(item)}, 200
        else:
            return {'error': {'message': 'Item not found'}}, 400
    
    def store(self, data: dict) -> dict:
        '''
        Accesses Model.save() to insert the item load by passed data and returns a list of saved items.
        '''
        item = self.model(**data)
        try:            
            item.save()
            items = self.get_all()

            return items
        except DataBaseException as e:
            return {'error': {'message': e.message}}, 500
    
    def update(self, _id, data: dict) -> dict:
        '''
        Accesses Model.save() to update the item found by passed id and returns a list of saved items.
        '''
        item = self.model.find_by_id(_id)
        if item:
            try:
                for field in data.keys(): 
                    setattr(item, field, verify_date_field(field, data[field]))
                item.save()
                items = self.get_all()

                return items
            except DataBaseException as e:
                return {'error': {'message': e.message}}, 500
        else:
            return {'error': {'message': 'Item not found'}}, 400
    
    def destroy(self, _id: int) -> dict:
        '''
        Accesses Model.delete() to delete the item found by passed id and returns a list of saved items.
        '''
        item = self.model.find_by_id(_id)
        if item:
            try:
                item.delete()
                items = self.get_all()

                return items
            except DataBaseException as e:
                return {'error': {'message': e.message}}, 500
        else:
            return {'error': {'message': 'Item not found'}}, 400