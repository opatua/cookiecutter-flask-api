from marshmallow import fields, Schema

from {{cookiecutter.app_name}}.models.user import UserModel


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    email = fields.Email(required=True)
    name = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
