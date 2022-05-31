from flask import Blueprint, jsonify, request
from flask_cors import CORS, cross_origin
from flask_restful import Api, Resource, marshal, reqparse, abort, fields, marshal_with
from model.models import db, PlayerBbrIdModel, PlayerInfoModel

player_info = Blueprint('player_info', __name__)

# delete player bbr id


@player_info.route('/player/bbr_id/<string:player_id>', methods=['DELETE'])
@cross_origin()
def delete_player_bbr_id(player_id):
    player = PlayerBbrIdModel.query.filter_by(id=player_id).first()
    if not player:
        abort(404, message="Player with that id doesn't exist...")
    db.session.delete(player)
    db.session.commit()
    return jsonify({'message': 'Player bbr id deleted'})


# post player bbr id


@player_info.route('/player/bbr_id/<string:player_id>', methods=['POST'])
@cross_origin()
def post_player_bbr_id(player_id):
    data = request.get_json()
    player = PlayerBbrIdModel(id=player_id, bbr_id=data['bbr_id'])
    db.session.add(player)
    db.session.commit()
    return jsonify({'message': 'Player bbr id added'})

# get player bbr id


@player_info.route('/player/bbr_id/<string:player_id>', methods=['GET'])
@cross_origin()
def get_player_bbr_id(player_id):
    player = PlayerBbrIdModel.query.filter_by(id=player_id).first()
    if not player:
        return jsonify({'message': 'No player found'})
    return jsonify({'bbr_id': player.bbr_id})

# delete player info


@player_info.route('/player/info/<string:player_id>', methods=['DELETE'])
@cross_origin()
def delete_player_info(player_id):
    player = PlayerInfoModel.query.filter_by(id=player_id).first()
    if not player:
        abort(404, message="Player with that id doesn't exist...")
    db.session.delete(player)
    db.session.commit()
    return jsonify({'message': 'Player deleted'})

# post player info


@player_info.route('/player/info/<string:player_id>', methods=['POST'])
@cross_origin()
def post_player_info(player_id):
    data = request.get_json()
    player = PlayerInfoModel(id=player_id, team_id=data['team_id'], first_name=data['first_name'], last_name=data['last_name'], pos_abbr=data['pos_abbr'], pos_full=data['pos_full'], jersey_number=data['jersey_number'], debut_year=data['debut_year'], years_pro=data['years_pro'], height_feet=data['height_feet'],
                             height_inches=data['height_inches'], height_meters=data['height_meters'], weight_pounds=data['weight_pounds'], weight_kilos=data['weight_kilos'], draft_team_id=data['draft_team_id'], draft_year=data['draft_year'], draft_round=data['draft_round'], draft_pick=data['draft_pick'], college=data['college'], country=data['country'])
    db.session.add(player)
    db.session.commit()
    return jsonify({'message': 'Player info added'})
