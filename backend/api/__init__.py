from flask import Blueprint, abort
from flask_restplus import Api, Resource, fields
from .models.user import User
from .models import db



blueprint = Blueprint('api', __name__)
api = Api(blueprint)

# User return model, hide all information which should be hidden
userModel = api.model('User', {
    'username': fields.String(required=True, description='Username for the user'),
})

# User create model, ensure password and email fields are included
userCreateModel = api.model('User', {
    'username': fields.String(required=True, description='Username for the user'),
    'password': fields.String(required=True, description='Password for the user'),
    'email':    fields.String(required=True, description='Email for the user')
})


@api.route('/users')
class UsersResource(Resource):
    
    @api.marshal_list_with(userModel)
    def get(self):
        '''Get all users'''
        users = User.query.all()
        return users

    @api.expect(userCreateModel)
    @api.marshal_with(userModel)
    def post(self):
        '''Create a new user'''
        data = api.payload
        
        if User.query.filter((User.username==data['username']) & (User.email==data['email'])).first():
            abort(400, 'Username or email address already exists')

        newUser = User(
            username=data['username'],
            email=data['email'])
        newUser.hash_password(data['password'])
        db.session.add(newUser)
        db.session.commit()
        return newUser
        



@api.route('/user/<username>')
class UserResource(Resource):

    @api.expect(userModel)
    @api.marshal_with(userModel)
    def get(self): 
        '''Get a user'''

    @api.expect(userModel)
    def put(self):
        '''Update a user'''
        data = api.payload
        return {'username': data['username'], 'password': data['password']}        