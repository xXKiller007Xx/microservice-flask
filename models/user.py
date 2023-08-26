from flask_restx import fields


class User:
    def __init__(self, api):
        self.api = api

    def get_user_model(self):
        return self.api.model('User', {
            'id': fields.Integer(required=True, description='User ID'),
            'name': fields.String(required=True, description='User Name'),
            'age': fields.Integer(description='User Age')
        })
