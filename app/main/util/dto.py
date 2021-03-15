from flask_restplus import Namespace, fields

# line 6 creates a new namespace for user related operations. Flask-RESTPlus provides a way to use almost the same pattern as Blueprint. The main idea is to split your app into reusable namespaces. A namespace module will contain models and resources declaration
# line 7 creates a new user dto through the model interface provided by the api namespace in line 6.
class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })
    
class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password'),
    })
