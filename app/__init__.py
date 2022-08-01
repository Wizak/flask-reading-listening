from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy()
api = Api(app)


from app.views import ReadBook, ReadText, WriteText, ReadSound


api.add_resource(ReadBook, '/book')
api.add_resource(ReadText, '/book/<title>')
api.add_resource(WriteText, '/text')
api.add_resource(ReadSound, '/sound/<title>')


def create_app(config_setting):
    app.config.from_object(config_setting)
    with app.test_request_context():
        db.init_app(app)
        db.create_all()

    return app
