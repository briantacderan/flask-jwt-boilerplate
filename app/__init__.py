# app/__init__.py

from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns


# Create a blueprint instance by passing name and import_name. API is the main entry point for the application resources and hence needs to be initialized with the blueprint


blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          doc='/documentation',
          title='FLASK RESTPLUS API BOILER-PLATE WITH JWT',
          version='1.0',
          description='Boilerplate for Flask-RESTPlus Web Service'
         )


# Add the user namespace user_ns to the list of namespaces in the API instance


api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns)
