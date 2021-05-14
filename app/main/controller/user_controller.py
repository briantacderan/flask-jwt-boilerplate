from flask import request
from flask_restplus import Resource

from ..util.dto import UserDto
from ..util.decorator import admin_token_required
from ..service.user_service import save_new_user, get_all_users, get_a_user


# The user controller class handles all the incoming HTTP requests relating to the user


api = UserDto.api
_user = UserDto.user


# Import all the required resources for the user controller


@api.route('/')
class UserList(Resource):
    @api.doc('list of registered users', security='Bearer Auth')
    @api.marshal_list_with(_user, envelope='data')
    @admin_token_required
    def get(self):
        """ List all registered users """
        return get_all_users()

    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    @api.expect(_user, validate=True)
    def post(self):
        """ Creates a new User """
        data = request.json
        return save_new_user(data=data)


@api.route('/<public_id>')
@api.param('public_id', 'The User identifier')
@api.response(404, 'User not found.')
class User(Resource):
    @api.doc('get a user')
    @api.marshal_with(_user)
    def get(self, public_id):
        """ Get a user given its identifier """
        user = get_a_user(public_id)
        if not user:
            api.abort(404)
        else:
            return user


# We defined two concrete classes in our user controller which are userList and user. These two classes extends the abstract flask-restplus resource

# Concrete resources should extend from this class and expose methods for each supported HTTP method. If a resource is invoked with an unsupported HTTP method, the API will return a response with status 405 Method Not Allowed. Otherwise the appropriate method is called and passed all arguments from the URL rule used when adding the resource to an API instance
