from flask_restx import Namespace, Resource
user_namespace = Namespace('users', description='User api')


@user_namespace.route('/')
class UserList(Resource):
    def get(self):
        return [{'id': 1, 'name': 'Thành'}, {'id': 2, 'name': 'Cường'}]
