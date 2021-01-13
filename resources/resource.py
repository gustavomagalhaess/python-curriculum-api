from models.model import Model, DataBaseException, string_to_date
import datetime
from typing import Optional

def non_empty_string(string: str) -> Exception:
    if not string:
        raise ValueError('Field must not be empty')

    return string

def verify_date_field(field, data: str) -> str:
    if field in ['started_at', 'ended_at', 'created_at', 'performed_at', 'issued_at', 'expires_at']:
        content = string_to_date(data)
    else:
        content = data

    return content

def check_json(item: Model) -> Optional[Model]:
        if item:
            return item.json()
        else:
            return None
    
def check_curriculum_json(item: Model) -> Optional[Model]:
    if item:
        return item.curriculum_json()
    else:
        return None

def list_map(collection: list) -> list:
    return list(map(lambda item: check_json(item), collection))

def list_map_curriculum(collection: list) -> list:
    return list(map(lambda item: check_curriculum_json(item), collection))

class Resource():

    def __init__(self, model: Model) -> None:
        self.model = model
    
    def get_all(self) -> dict:
        items = self.model.get_all()

        return {'items': list_map(items)}, 200
    
    def find_by_id(self, _id: int) -> dict:
        item = self.model.find_by_id(_id)
        if item:
            return {'item': check_json(item)}, 200
        else:
            return {'error': {'message': 'Item not found'}}, 400
    
    def store(self, data: dict) -> dict:
        item = self.model(**data)
        try:            
            item.save()
            items = self.get_all()

            return items
        except DataBaseException as e:
            return {'error': {'message': e.message}}, 500
    
    def update(self, _id, data: dict) -> dict:
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