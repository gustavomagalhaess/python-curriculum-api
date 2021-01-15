'''
User Resource Module

This module contains only user resource methods.
'''

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
from models.model import Model, DataBaseException, string_to_date
from models.user import UserModel
from resources.resource import non_empty_string
from blacklist import BLACKLIST

parser = reqparse.RequestParser()
parser.add_argument('username', type=non_empty_string, required=True, help='Required field')
parser.add_argument('password', type=non_empty_string, required=True, help='Required field')

class User(Resource, ResourceHelper):
    '''
    User Resource Class

    This class contains only user resource methods.
    '''
    def __init__(self, model: Model = UserModel) -> None:
        '''
        User Resource Constructor

        Loads the UserModel passed as param.
        '''
        super().__init__(model)
    
    @jwt_required
    def get(self, _id: int) -> dict:
        '''
        Accesses UserModel.get_all() and returns the serached user by id. The user is allowed to 
        access your own data.
        '''
        current_user = get_jwt_identity()
        user = self.model.find_by_id(_id)
        if current_user and user and current_user == user.id:
            return user.json()
        else:
            return {'error': {'message': 'Forbidden request.'}}, 403


class ChangePassword(Resource):
    '''
    ChangePassword Resource Class

    This module contains only a method to change the password.
    '''
    def __init__(self, model: Model = UserModel) -> None:
        '''
        ChangePassword Resource Constructor

        Loads the UserModel passed as param.
        '''
        self.model = model
    
    def put(self):
        #TODO Implement by access link
        pass

 
class Login(Resource):
    '''
    Login Resource Class

    This module contains only a method to login the user in app.
    '''
    def __init__(self, model: Model = UserModel) -> None:
        '''
        Login Resource Constructor

        Loads the UserModel passed as param.
        '''
        self.model = model

    def post(self) -> dict:
        '''
        Accesses UserModel.find_by_username(), checks the user's credentials passed in request and 
        return an access token and a refresh token if the user's credentials are right.
        '''
        data = parser.parse_args()
        user = self.model.find_by_username(data['username'])
        if user and safe_str_cmp(user.password, data['password']):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)

            return {'access_token': access_token, 'refresh_token': refresh_token}, 200

        return {'error': {'message': 'Invalid Credentials.'}}, 401


class Logout(Resource):
    '''
    Logout Resource Class

    This module contains only a method to logout the user from app.
    '''
    @jwt_required
    def post(self) -> dict:
        '''
        Logouts the user from app.
        '''
        jti = get_raw_jwt()['jti']
        BLACKLIST.add(jti)

        return {'message': 'Successfully logged out.'}, 200


class TokenRefresh(Resource):
    '''
    TokenRefresh Resource Class

    This module contains only a method to refresh the user's access token when expired.
    '''
    @jwt_refresh_token_required
    def post(self) -> dict:
        '''
        Refreshes the user's access token.
        '''
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=False)

        return {'access_token': new_token}, 200