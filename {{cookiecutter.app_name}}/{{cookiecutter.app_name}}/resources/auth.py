from flask import request, jsonify
from flask_restful import Resource
from http import HTTPStatus
from marshmallow import ValidationError

from {{cookiecutter.app_name}}.libs.authentication import Auth
from {{cookiecutter.app_name}}.models import UserModel
from {{cookiecutter.app_name}}.schemas import UserSchema

user_schema = UserSchema()

REQUEST_NOT_VALID = 'Request not valid.'
USER_NOT_FOUND = 'User not found.'
USER_EXISTS = 'User exists.'
USER_INVALID_CREDENTIAL = 'Invalid credential.'


class Login(Resource):

    @classmethod
    def post(self):
        user_json = request.get_json()

        data, error = user_schema.load(user_json, partial=True)

        if error:
            return {'message': REQUEST_NOT_VALID}, HTTPStatus.BAD_REQUEST
        if not data.get('email') or not data.get('password'):
            return {'message': REQUEST_NOT_VALID}, HTTPStatus.BAD_REQUEST

        user = UserModel.query.filter_by(email=data.get('email')).first()

        if not user:
            return {'message': USER_NOT_FOUND}, HTTPStatus.BAD_REQUEST
        if not user.check_hash(data.get('password')):
            return {'message': USER_INVALID_CREDENTIAL}, HTTPStatus.BAD_REQUEST

        token = Auth.generate_token(user)
        payload = {
            "token": token,
            "user": {
                "id": user.id,
                "email": user.email,
                "name": user.name,
                "is_active": user.is_active
            }
        }
        return jsonify(payload)


class Register(Resource):
    @classmethod
    def post(self):
        user_json = request.get_json()

        data, error = user_schema.load(user_json, partial=True)

        if error:
            return {'message': REQUEST_NOT_VALID}, HTTPStatus.BAD_REQUEST
        if not data.get('email') or not data.get('password') or not data.get('name'):
            return {'message': REQUEST_NOT_VALID}, HTTPStatus.BAD_REQUEST

        is_exist = UserModel.query.filter_by(email=data.get('email')).first()

        if is_exist != None:
            return {'message': USER_EXISTS}, HTTPStatus.BAD_REQUEST

        user = UserModel(data)
        user.save()
        data = user_schema.dump(user).data

        payload = {
            'message': 'success',
            'data': data
        }

        return jsonify(payload)
