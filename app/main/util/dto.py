from flask_restplus import Namespace, fields

authorizations = {
    'Bearer Auth': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}


class UserDto:
    api = Namespace(
        'user', 
        description='User related operations'
    )
    user = api.model('user', {
        'email': fields.String(required=True, description='User email address'),
        'username': fields.String(required=True, description='User username'),
        'password': fields.String(required=True, description='User password'),
        'public_id': fields.String(description='User Identifier')
    })
    
class AuthDto:
    api = Namespace(
        'auth', 
        description='Authentication related operations',
        authorizations=authorizations
    )
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password')
    })
