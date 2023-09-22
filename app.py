# Import
from flask import Flask
from flask_restx import Api, Resource
from controllers.user_controller import user_namespace, GetAllUser;



# Dependency Injection



# Define the app Flask
app = Flask(__name__)

api = Api(app, version='1.0', title='API',
          description='A simple API with Swagger documentation')
api.add_namespace(user_namespace)


if __name__ == '__main__':
    app.run(debug=True, port=8080)
