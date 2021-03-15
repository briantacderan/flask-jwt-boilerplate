# app/__init__.py

from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns

# In line 10, we create a blueprint instance by passing name and import_name. API is the main entry point for the application resources and hence needs to be initialized with the blueprint in line 12

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS API BOILER-PLATE WITH JWT',
          version='1.0',
          description='a boilerplate for flask restplus web service'
          )

api.add_namespace(user_ns, path='/user')

# In line 18 , we add the user namespace user_ns to the list of namespaces in the API instance
# 
# We have now defined our blueprint. It’s time to register it on our Flask app
# Update manage.py by importing blueprint and registering it with the Flask application instance.
