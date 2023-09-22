from flask_restx import Namespace, Resource, reqparse
from flask import request
from config import Config
from utils.querieHelper import QueriesHelper

user_namespace = Namespace('users', description='User api')
parser = reqparse.RequestParser()


@user_namespace.route('/')
class GetAllUser(Resource):
    def get(self):
        try:
            username = request.args.get("username") or ""
            return QueriesHelper.getFirst(f"SELECT * FROM Users WHERE Username = '{username}'")
        except Exception as ex:
            return {
                "Msg": str(ex)
            }, 500
