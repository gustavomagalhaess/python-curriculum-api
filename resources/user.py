from flask_restful import Resource, reqparse
from resources.resource import Resource as ResourceHelper
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_refresh_token_required,
    get_jwt_identity,
    get_raw_jwt,
    jwt_required
)
from models.model import DataBaseException, string_to_date
from models.user import UserModel
from resources.resource import non_empty_string
from blacklist import BLACKLIST

parser = reqparse.RequestParser()
parser.add_argument('username', type=non_empty_string, required=True, help='Required field')
parser.add_argument('password', type=non_empty_string, required=True, help='Required field')

class User(Resource, ResourceHelper):

    def __init__(self, model = UserModel):
        super().__init__(model)
    
    @jwt_required
    def get(self, _id):
        current_user = get_jwt_identity()
        user = self.model.find_by_id(_id)
        if current_user and user and current_user == user.id:
            return user.json()
        else:
            return {'error': {'message': 'Forbidden request.'}}, 403


class ChangePassword(Resource):
    def __init__(self, model = UserModel):
            self.model = model
    
    def put(self):
        #TODO Implement by access link
        pass

 
class Login(Resource):

    def __init__(self, model = UserModel):
        self.model = model

    def post(self):
        data = parser.parse_args()
        user = self.model.find_by_username(data['username'])
        if user and safe_str_cmp(user.password, data['password']):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)

            return {'access_token': access_token, 'refresh_token': refresh_token}, 200

        return {'error': {'message': 'Invalid Credentials.'}}, 401


class Logout(Resource):

    @jwt_required
    def post(self):
        jti = get_raw_jwt()['jti']
        BLACKLIST.add(jti)

        return {'message': 'Successfully logged out.'}, 200


class TokenRefresh(Resource):

    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=False)

        return {'access_token': new_token}, 200