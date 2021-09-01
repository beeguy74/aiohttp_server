from app.web.schemes import OkResponseSchema
from marshmallow import Schema, fields, schema


class UserAddSchema(Schema):
    email = fields.Str(required=True)

class UserSchema(UserAddSchema):
    id = fields.UUID(required=True)

class UserGetRequestSchema(Schema):
    id = fields.UUID(required=True)

class UserGetSchema(Schema):
    user = fields.Nested(UserSchema)

class UserGetResponseSchema(OkResponseSchema):
    data = fields.Nested(UserGetSchema)

class ListUsersSchema(Schema):
    users = fields.Nested(UserSchema, many=True)

class ListUsersResponseSchema(OkResponseSchema):
    data = fields.Nested(ListUsersSchema)