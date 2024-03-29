from flask import Flask

def create_app(config_name):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost:3306/tutorial_canciones'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return app
