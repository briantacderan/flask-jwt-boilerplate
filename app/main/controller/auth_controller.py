from flask import request
from flask_restplus import Resource, marshal, fields

from app.main.service.auth_helper import Auth
from ..util.dto import AuthDto
from ..util.decorator import token_required

import requests

api = AuthDto.api
user_auth = AuthDto.user_auth


@api.route('/login')
class UserLogin(Resource):
    @api.doc('user login')
    @api.expect(user_auth, validate=True)
    def post(self):
        """ User login resource """
        post_data = request.json
        resp = Auth.login_user(data=post_data)
        api.header = {'Authorization': f'Bearer {resp[0]["Authorization"]}'}
        return resp


@api.route('/logout')
class LogoutAPI(Resource):
    @api.doc('logout a user', security='Bearer Auth')
    @token_required
    def post(self):
        """ User logout resource """
        return Auth.logout_user(data=api.header)
