import numpy as np
from flask import Flask,request,render_template
from . import predict,index
import os
import sys
import pickle


def create_app():
    #Defining flask object
    app=Flask(__name__,instance_relative_config=True)
    #defining load_dotenv object
    #..
    #..
    #Creating instansce path
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.register_blueprint(index.bp)
    app.register_blueprint(predict.bp)
    
    return app

