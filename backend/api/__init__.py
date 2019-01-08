from flask import Blueprint
from flask_restplus import Api, Resource, fields

blueprint = Blueprint('api', __name__)
api = Api(blueprint)


@api.route('/user')
class UserResource(Resource):
    model = api.model('User', {
        'username': fields.String(required=True, description='Username for the user'),
        'password': fields.String(required=True, description='Password for the user')
    })

    @api.doc('get user')
    def get(self):
        return {'hello': 'world'}

    @api.expect(model)
    def post(self):
        data = api.payload
        return {'username': data['username'], 'password': data['password']}