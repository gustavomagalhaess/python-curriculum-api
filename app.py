#Including paths
import sys
sys.path.insert(0, '/database/')

from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager

from database.db import db
from blacklist import BLACKLIST

#Resources
from resources.curriculum import Curriculum
from resources.segment import Segment, SegmentList
from resources.resume import Resume, ResumeList
from resources.graduation import Graduation, GraduationList
from resources.certification import Certification, CertificationList
from resources.skill import Skill, SkillList
from resources.company import Company, CompanyList
from resources.product import Product, ProductList
from resources.presentation import Presentation, PresentationList
from resources.user import User, Login, Logout, TokenRefresh, ChangePassword

#Configs
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
api = Api(app)

#JWT configs
app.config['JWT_SECRET_KEY'] = 'mySecretKey'# Change this!
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
jwt = JWTManager(app)

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    return decrypted_token['jti'] in BLACKLIST

@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({'error': {'message': 'Signature verification failed.'}}), 401

@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify({'error': {'message': 'Request does not contain an access token.'}}), 401

@jwt.needs_fresh_token_loader
def token_not_fresh_callback():
    return jsonify({'error': {'message': 'The token is not fresh.'}}), 401

@jwt.revoked_token_loader
def revoked_token_callback():
    return jsonify({'error': {'message': 'The token has been revoked.'}}), 401
#JWT configs ends

#Routes
api.add_resource(Curriculum, '/curriculum/<int:segment_id>')
api.add_resource(Segment, '/segment/<int:_id>')
api.add_resource(SegmentList, '/segments')  
api.add_resource(Resume, '/resume/<int:_id>')
api.add_resource(ResumeList, '/resumes')
api.add_resource(Graduation, '/graduation/<int:_id>')
api.add_resource(GraduationList, '/graduations')
api.add_resource(Certification, '/certification/<int:_id>')
api.add_resource(CertificationList, '/certifications')
api.add_resource(Skill, '/skill/<int:_id>')
api.add_resource(SkillList, '/skills')
api.add_resource(Company, '/company/<int:_id>')
api.add_resource(CompanyList, '/companies')
api.add_resource(Product, '/product/<int:_id>')
api.add_resource(ProductList, '/products')
api.add_resource(Presentation, '/presentation/<int:_id>')
api.add_resource(PresentationList, '/presentations')
api.add_resource(User, '/user/<int:_id>')
api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')
api.add_resource(TokenRefresh, '/refresh')
#api.add_resource(ChangePassword, '/change-password')


if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)