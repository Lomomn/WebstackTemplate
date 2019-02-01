from flask import Blueprint, abort, jsonify
from flask_restplus import Namespace, Resource, fields
from .models.user import User
from .models import db

api = Namespace('users', description='User related operations')

# User return model, hide all information which should be hidden
userReturnModel = api.model('UserReturnModel', {
    'username': fields.String(required=True, description='Username for the user'),
})

# User create model, ensure password and email fields are included
userCreateModel = api.model('UserCreateModel', {
    'username': fields.String(required=True, description='Username for the user'),
    'password': fields.String(required=True, description='Password for the user'),
    'email':    fields.String(required=True, description='Email for the user')
})

# User login model, accepts username with a password
userLoginModel = api.model('UserLoginModel', {
    'username': fields.String(required=True, description='Username for the user'),
    'password': fields.String(required=True, description='Password for the user')
})

# Return user auth token
userReturnLoginModel = api.model('UserReturnLoginModel', {
    'token': fields.String(required=True, description='Return auth token')
})


@api.route('/', endpoint='users')
class UsersResource(Resource):
    
    @api.marshal_list_with(userReturnModel)
    def get(self):
        '''Get all users'''
        users = User.query.all()
        return users

    @api.expect(userCreateModel)
    @api.marshal_with(userReturnModel)
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
        

@api.route('/<username>/', endpoint='user')
class UserResource(Resource):

    @api.expect(userReturnModel)
    @api.marshal_with(userReturnModel)
    def get(self): 
        '''Get a user'''

    @api.expect(userReturnModel)
    def put(self):
        '''Update a user'''
        data = api.payload
        

@api.route('/login/', endpoint='login')
class Login(Resource):
    
    @api.expect(userLoginModel)
    @api.marshal_with(userReturnLoginModel)
    def post(self):
        data = api.payload
        user = User.query.filter(User.username==data['username']).first()
        if not user:
            abort(401)

        token = user.generate_auth_token()
        user.token = token
        return user
            


