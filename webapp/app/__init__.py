from flask import Flask
#from flask import g
from config import config
import os

# Creates our application.
app = Flask(__name__)
config_name = os.getenv('FLASK_CONFIG') or 'default'
app.config.from_object(config[config_name])
config[config_name].init_app(app)


from app import views, errors
