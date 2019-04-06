import jwt
import os
import datetime

from flask import json, Response, request, g
from http import HTTPStatus
from functools import wraps
from {{cookiecutter.app_name}}.models.user import UserModel


class Auth():

    @staticmethod
    def generate_token(user):
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=20),
            'iat': datetime.datetime.utcnow(),
            'id': user.id,
            'email': user.email,
            'name': user.name,
            'is_active': user.is_active
        }
        return jwt.encode(payload, os.getenv('JWT_SECRET_KEY'), 'HS256',).decode("utf-8")

    @staticmethod
    def decode_token(token):
        result = {'data': {}, 'error': {}}
        try:
            payload = jwt.decode(token, os.getenv('JWT_SECRET_KEY'))
            result['data'] = {'user_id': payload['id']}
            return result

        except jwt.ExpiredSignatureError as signatureError:
            result['error'] = {'message': 'Token Expired'}
            return result

        except jwt.InvalidTokenError as invalidToken:
            result['error'] = {'message': 'Permission Denied'}
            return result

    @staticmethod
    def login_required(func):

        @wraps(func)
        def decorated_auth(*args, **kwargs):

            if 'Bearer' not in request.headers:
                return Response(
                    mimetype="application/json",
                    response=json.dumps({'error': 'Permission Denied'}),
                    status=HTTPStatus.BAD_REQUEST
                )

            token = request.headers.get('Bearer')
            data = Auth.decode_token(token)
            if data['error']:
                return Response(
                    mimetype="application/json",
                    response=json.dumps(data['error']),
                    status=HTTPStatus.BAD_REQUEST
                )

            user_id = data['data']['user_id']
            check_user = UserModel.query.filter_by(id=user_id).first()

            if not check_user:
                return Response(
                    mimetype="application/json",
                    response=json.dumps({'error': 'Permission Denied'}),
                    status=HTTPStatus.BAD_REQUEST
                )

            g.user = {'id': user_id}
            return func(*args, **kwargs)

        return decorated_auth
