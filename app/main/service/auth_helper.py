import jwt
from app.main.model.user import User
from ..service.blacklist_service import save_token
from ..config import key

from ..util.dto import AuthDto
api = AuthDto.api

class Auth:
    @staticmethod
    def login_user(data):
        try:
            user = User.query.filter_by(email=data.get('email')).first()
            if user and user.check_password(data.get('password')):
                auth_token = user.encode_auth_token(user.id)
                if auth_token:
                    response_object = {
                        'status': 'success',
                        'message': 'Successfully logged in.',
                        'Authorization': auth_token.decode()
                    }
                    return response_object, 200
            else:
                response_object = {
                    'status': 'fail',
                    'message': 'Email or password does not match.'
                }
                return response_object, 401

        except Exception as e:
            print(e)
            response_object = {
                'status': 'fail',
                'message': 'Try again'
            }
            return response_object, 500

    @staticmethod
    def logout_user(data):
        if User.is_valid_token_format(data):
            auth_token = data['Authorization'].split(' ')[1]
        else:
            auth_token = ''
        resp = User.decode_auth_token(auth_token)
        if auth_token:
            if not isinstance(resp, str):
                return save_token(token=auth_token)
            else:
                code_list = {
                    'Token blacklisted': 403,
                    'Invalid token': 403
                }
                response_object = {
                    'status': 'fail',
                    'message': resp
                }
                return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 401

    # @staticmethod
    def get_logged_in_user(new_request):
        """ Get the auth token """
        try:
            auth_head = new_request.headers.get('Authorization')
        except:
            auth_head = new_request['Authorization']
        else:
            auth_head = api.header['Authorization']
        auth_token = auth_head.split(' ')[-1]
        resp = User.decode_auth_token(auth_token)
        if not isinstance(resp, str):
            user = User.query.filter_by(id=resp).first()
            response_object = {
                'status': 'success',
                'data': {
                    'user_id': user.id,
                    'email': user.email,
                    'admin': user.admin,
                    'registered_on': str(user.registered_on)
                }
            }
            return response_object, 200
        else:
            response_object = {
                'status': 'fail',
                'message': resp
                # 'message': 'Provide a valid auth token.'
            }
            return response_object, 401
