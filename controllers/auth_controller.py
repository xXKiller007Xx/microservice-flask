from flask_restx import Namespace, Resource, reqparse, fields
from flask import request
from utils.querieHelper import QueriesHelper
from flask_jwt_extended import jwt_required
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
import uuid

auth_namespace = Namespace('auth', description='Auth api')
parser = reqparse.RequestParser()


@auth_namespace.route("/login")
class Login(Resource):
    login_field = auth_namespace.model('Login', {
        'username': fields.String,
        'password': fields.String
    })
    @auth_namespace.expect(login_field)
    def post(self):
        try:
            content_type = request.headers.get('Content-Type')
            username = ""
            if (content_type == "application/json"):
                json = request.json
                username = json['username'] or None
                password = json['password'] or None
                data = QueriesHelper.getFirst(
                    "SELECT Username FROM Users WHERE Username = ? AND Password = ?", (username, password))
                if data is not None:
                    return create_access_token(identity=username)
                # parse data
                return {
                    "Msg": "Username or password is incorrect"
                }, 400
        except Exception as ex:
            return {
                "Msg": str(ex)
            }, 500
            
@auth_namespace.route("/register")
class Register(Resource):
    register_field = auth_namespace.model('register', {
        'username': fields.String,
        'password': fields.String
    })
    @auth_namespace.expect(register_field)
    def post(self):
        try:
            content_type = request.headers.get('Content-Type')
            username = ""
            if (content_type == "application/json"):
                json = request.json
                username = json['username']
                password = json['password']
                if (username is None or "") and (password is None or ""):
                    return  {
                    "Msg": "Username and password is required"
                }, 400
                    
                data = QueriesHelper.getFirst(
                    "SELECT Username FROM Users WHERE Username = ? AND Password = ?", (username, password))
                if data is not None:
                    return create_access_token(identity=username)
                # parse data
                return {
                    "Msg": "Username or password is incorrect"
                }, 400
        except Exception as ex:
            return {
                "Msg": str(ex)
            }, 500
