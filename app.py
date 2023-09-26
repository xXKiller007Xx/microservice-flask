from config import Config
from flask import Flask
from flask_restx import Api, Resource
from controllers.user_controller import user_namespace
from controllers.product_controller import product_namespace
from controllers.cart_controller import cart_namespace
from controllers.auth_controller import auth_namespace


from flask_jwt_extended import JWTManager
# Define the app Flask
app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = Config.JWT_SECRET_KEY
jwt = JWTManager(app)

api = Api(app, version='1.0', title='API',
          description='A simple API with Swagger documentation')

api.add_namespace(user_namespace)
api.add_namespace(product_namespace)
api.add_namespace(cart_namespace)
api.add_namespace(auth_namespace)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
