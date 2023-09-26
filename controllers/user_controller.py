from flask_restx import Namespace, Resource, reqparse
from flask import request
from utils.querieHelper import QueriesHelper
from flask_jwt_extended import jwt_required

user_namespace = Namespace('users', description='User api')
parser = reqparse.RequestParser()


@user_namespace.route('/')
class GetAllUser(Resource):
    #@jwt_required()
    def get(self):
        try:
            content_type = request.headers.get('Content-Type')
            if (content_type == "application/json"):
                json = request.json
                # parse data
                return json
            #username = request.args.get("username") or ""
            #return QueriesHelper.getFirst(f"SELECT * FROM Users WHERE Username = '{username}'")
        except Exception as ex:
            return {
                "Msg": str(ex)
            }, 500
