from flask import Flask, jsonify, request
from flask_restful import Api, Resource, marshal, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from model.models import db
from routes.player_info import player_info
from routes.player_basic import player_basic
from routes.player_advanced import player_advanced
from routes.player_analysis import player_analysis
from routes.player_get import player_get_stats
from routes.team_info import team_info
from routes.team_stats import team_stats
from routes.team_get import team_get

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://snbhmwkhirenmk:4322db215c2e5a3817b871e245bce4c8d8ef0b6b4af179daf54718e938ff34d7@ec2-52-3-60-53.compute-1.amazonaws.com:5432/d96kme5om0k14h'
db.init_app(app)

app.register_blueprint(player_info)
app.register_blueprint(player_basic)
app.register_blueprint(player_advanced)
app.register_blueprint(player_analysis)
app.register_blueprint(player_get_stats)
app.register_blueprint(team_info)
app.register_blueprint(team_stats)
app.register_blueprint(team_get)


if '__main__' == __name__:
    app.run(debug=True)
