from flask_restplus import Namespace, fields
# from .decorator import token_required, admin_token_required

# As the name implies, the data transfer object (DTO) will be responsible for carrying data between processes. In our own case, it will be used for marshaling data for our API calls. We will understand this better as we proceed.


authorizations = {
    'Bearer Auth': {
        'type': 'apiKey',
        'in': 'headers',
        'name': 'Authorization'
    }
}


# Create a new namespace for user related operations. Flask-RESTPlus provides a way to use almost the same pattern as Blueprint. The main idea is to split your app into reusable namespaces. A namespace module will contain models and resources declaration

class UserDto:
    api = Namespace(
        'user', 
        description='User related operations',
        authorizations=authorizations
    )
    
    # Create a new user dto through the model interface provided by the api namespace
    
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
        'email': fields.String(required=True, 
                               description='Email address for login'),
        'password': fields.String(required=True, 
                                  description='User password for login')
    })
