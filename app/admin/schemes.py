from marshmallow import Schema, fields


class AdminSchema(Schema):
    email = fields.Email()
    password = fields.Str()

class AdminResponseSchema(Schema):
    id = fields.Int()
    email = fields.Email()