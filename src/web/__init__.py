from flask import Flask, render_template
from flask import url_for
from flask import redirect
from datetime import datetime 
from src.web.controllers.api import api_blueprint


def create_app(env="development", static_folder="static"):

    app = Flask(__name__, static_folder=static_folder)

    app.jinja_env.globals.update(datetime=datetime)

    app.register_blueprint(api_blueprint)
    

    @app.get("/")
    def entry_point():
        return render_template('dashboard.html')

    return app