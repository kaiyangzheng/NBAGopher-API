from flask import Flask, jsonify, request, make_response
from flask_restful import Api, Resource, marshal, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from model.models import db, UserModel
from routes.player_info import player_info
from routes.player_basic import player_basic
from routes.player_advanced import player_advanced
from routes.player_analysis import player_analysis
from routes.player_get import player_get_stats
from routes.team_info import team_info
from routes.team_stats import team_stats
from routes.team_get import team_get
from routes.team_analysis import team_analysis
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import re
import uuid
import datetime

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
app.register_blueprint(team_analysis)


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        try:
            data = jwt.decode(
                token, app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = UserModel.query.filter_by(
                public_id=data['public_id']).first()
        except:
            return jsonify({'message': 'Token is invalid!'}), 401
        return f(current_user, *args, **kwargs)
    return decorated


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    name = data['name']
    email = data['email']
    password = data['password']
    if len(password) < 6:
        return jsonify({'message': 'Password too short! Must be at least 6 characters long.'})
    if len(name) < 3:
        return jsonify({'message': 'Name too short! Must be at least 3 characters long.'})
    if not name.isalnum() or " " in name:
        return jsonify({'error': "Name should be alphanumeric and include no spaces"}), 400
    if UserModel.query.filter_by(name=name).first() is not None:
        return jsonify({'error': "Name is taken"}), 409
    if UserModel.query.filter_by(email=email).first() is not None:
        return jsonify({'error': "Email is taken"}), 409
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return jsonify({'error': "Invalid email"}), 400
    hashed_password = generate_password_hash(
        data['password'], method='sha256')
    new_user = UserModel(public_id=str(uuid.uuid4()), name=name,
                         password=hashed_password, email=email, admin=False)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'Registration successful!'})


@app.route('/login', methods=['POST'])
def login():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})
    user = UserModel.query.filter_by(name=auth.username).first()
    if not user:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})
    if check_password_hash(user.password, auth.password):
        token = jwt.encode({'public_id': user.public_id, 'exp': datetime.datetime.utcnow(
        ) + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
        return jsonify({'token': token})
    return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})


if '__main__' == __name__:
    app.run(debug=True)
