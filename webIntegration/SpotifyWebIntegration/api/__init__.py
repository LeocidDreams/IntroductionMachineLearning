from flask import Flask
import logging
import os
import sys
# from api import routes
# from api import index
from api import routes
from api import index

def create_app():
    #defining flask object
    app=Flask(__name__,instance_relative_config=True)
    app.logger.setLevel(logging.INFO)

    #Defining load_dotenv object
    #...
    #loading Environment variables
    #...

    #Creating instance path
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.register_blueprint(index.bp)
    app.register_blueprint(routes.bp)


    return app