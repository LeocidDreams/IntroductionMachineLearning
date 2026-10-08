#importing flask library
from flask import Flask,render_template
from flask import render_template_string,request,Response,redirect

from api import suggestion

import os
import sys
from dotenv import load_dotenv
load_dotenv()


def create_app(test_config=None):
    app=Flask(__name__,instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=os.getenv('SECRET_KEY'),
        API_KEY=os.getenv('API_KEY')
    )
    if test_config is None:
        #load the instance config,if it exists,when not testing
        app.config.from_pyfile('config.py',silent=True)
    else:
        #load the test config if passed in
        app.config.from_mapping(test_config)

    #ensure the instance folder exists
    os.makedirs(app.instance_path,exist_ok=True)

    app.register_blueprint(suggestion.bp)

    @app.route('/',methods=['POST','GET'])
    def index():
        return render_template('base.html')

