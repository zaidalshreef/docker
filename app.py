import os
import datetime
from flask import Flask, request, abort, jsonify,session,redirect,render_template,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from urllib.parse import urlencode



def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             "Content-Type,Authorization,true")
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PUT,POST,PATCH,DELETE,OPTIONS')
        return response

  
    @app.route('/')
    def view():
        
        return jsonify({"success": True,
                        "greeting": "hello world",
                        })

    return app


app = create_app()

if __name__ == '__main__':
    app.run(port=8080, debug=True)
