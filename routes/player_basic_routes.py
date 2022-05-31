from flask import Blueprint, jsonify, request
from flask_cors import CORS, cross_origin
from flask_restful import Api, Resource, marshal, reqparse, abort, fields, marshal_with
from models import db, PlayerBasicLatestModel, PlayerBasicCareerModel, PlayerBasicLatestPctlModel, PlayerBasicPrevModel, PlayerBasicPrevPctlModel, PlayerBasicSeason

player_basic = Blueprint('player_basic', __name__)

# delete player basic latest


@player_basic.route('/player/basic_latest/<string:player_id>', methods=['DELETE'])
@cross_origin()
def delete_player_basic_latest(player_id):
    player = PlayerBasicLatestModel.query.filter_by(id=player_id).first()
    if not player:
        abort(404, message="Player with that id doesn't exist...")
    db.session.delete(player)
    db.session.commit()
    return jsonify({'message': 'Player basic latest deleted'})

# post player basic latest


@player_basic.route('/player/basic_latest/<string:player_id>', methods=['POST'])
@cross_origin()
def post_player_basic_latest(player_id):
    data = request.get_json()
    player = PlayerBasicLatestModel(id=player_id, mpg=data['mpg'], games_played=data['games_played'], games_started=data['games_started'], ppg=data['ppg'], apg=data['apg'], rpg=data['rpg'], spg=data['spg'],
                                    bpg=data['bpg'], topg=data['topg'], pfpg=data['pfpg'], fta=data['fta'], ftm=data['ftm'], ftp=data['ftp'], fga=data['fga'], fgm=data['fgm'], fgp=data['fgp'], tpa=data['tpa'], tpm=data['tpm'], tpp=data['tpp'])
    db.session.add(player)
    db.session.commit()
    return jsonify({'message': 'Player basic latest added'})

# delete player basic career


@player_basic.route('/player/basic_career/<string:player_id>', methods=['DELETE'])
@cross_origin()
def delete_player_basic_career(player_id):
    player = PlayerBasicCareerModel.query.filter_by(id=player_id).first()
    if not player:
        abort(404, message="Player with that id doesn't exist...")
    db.session.delete(player)
    db.session.commit()
    return jsonify({'message': 'Player basic career deleted'})

# post player basic career


@player_basic.route('/player/basic_career/<string:player_id>', methods=['POST'])
@cross_origin()
def post_player_basic_career(player_id):
    data = request.get_json()
    player = PlayerBasicCareerModel(id=player_id, mpg=data['mpg'], games_played=data['games_played'], games_started=data['games_started'], ppg=data['ppg'], apg=data['apg'], rpg=data['rpg'], spg=data['spg'],
                                    bpg=data['bpg'], topg=data['topg'], pfpg=data['pfpg'], fta=data['fta'], ftm=data['ftm'], ftp=data['ftp'], fga=data['fga'], fgm=data['fgm'], fgp=data['fgp'], tpa=data['tpa'], tpm=data['tpm'], tpp=data['tpp'])
    db.session.add(player)
    db.session.commit()
    return jsonify({'message': 'Player basic career added'})

# delete player basic latest pctls


@player_basic.route('/player/basic_latest_pctls/<string:player_id>', methods=['DELETE'])
@cross_origin()
def delete_player_basic_latest_pctls(player_id):
    player = PlayerBasicLatestPctlModel.query.filter_by(id=player_id).first()
    if not player:
        abort(404, message="Player with that id doesn't exist...")
    db.session.delete(player)
    db.session.commit()
    return jsonify({'message': 'Player basic latest pctls deleted'})

# post player basic latest pctls


@player_basic.route('/player/basic_latest_pctls/<string:player_id>', methods=['POST'])
@cross_origin()
def post_player_basic_latest_pctls(player_id):
    data = request.get_json()
    player = PlayerBasicLatestPctlModel(id=player_id, mpg=data['mpg'], games_played=data['games_played'], games_started=data['games_started'], ppg=data['ppg'], apg=data['apg'], rpg=data['rpg'], spg=data['spg'],
                                        bpg=data['bpg'], topg=data['topg'], pfpg=data['pfpg'], fta=data['fta'], ftm=data['ftm'], ftp=data['ftp'], fga=data['fga'], fgm=data['fgm'], fgp=data['fgp'], tpa=data['tpa'], tpm=data['tpm'], tpp=data['tpp'])
    db.session.add(player)
    db.session.commit()
    return jsonify({'message': 'Player basic latest pctls added'})

# post basic prev stats


@player_basic.route('/player/basic_prev_stats/<string:player_id>', methods=['POST'])
@cross_origin()
def post_player_basic_prev_stats(player_id):
    data = request.get_json()
    player = PlayerBasicPrevModel(id=player_id, mpg=data['mpg'], games_played=data['games_played'], games_started=data['games_started'], ppg=data['ppg'], apg=data['apg'], rpg=data['rpg'], spg=data['spg'],
                                  bpg=data['bpg'], topg=data['topg'], pfpg=data['pfpg'], fta=data['fta'], ftm=data['ftm'], ftp=data['ftp'], fga=data['fga'], fgm=data['fgm'], fgp=data['fgp'], tpa=data['tpa'], tpm=data['tpm'], tpp=data['tpp'])
    db.session.add(player)
    db.session.commit()
    return jsonify({'message': 'Player basic prev stats added'})

# delete basic prev stats


@player_basic.route('/player/basic_prev_stats/<string:player_id>', methods=['DELETE'])
@cross_origin()
def delete_player_basic_prev_stats(player_id):
    player = PlayerBasicPrevModel.query.filter_by(id=player_id).first()
    if not player:
        abort(404, message="Player with that id doesn't exist...")
    db.session.delete(player)
    db.session.commit()
    return jsonify({'message': 'Player basic prev stats deleted'})

# post basic prev pctls


@player_basic.route('/player/basic_prev_pctls/<string:player_id>', methods=['POST'])
@cross_origin()
def post_player_basic_prev_pctls(player_id):
    data = request.get_json()
    player = PlayerBasicPrevPctlModel(id=player_id, mpg=data['mpg'], games_played=data['games_played'], games_started=data['games_started'], ppg=data['ppg'], apg=data['apg'], rpg=data['rpg'], spg=data['spg'],
                                      bpg=data['bpg'], topg=data['topg'], pfpg=data['pfpg'], fta=data['fta'], ftm=data['ftm'], ftp=data['ftp'], fga=data['fga'], fgm=data['fgm'], fgp=data['fgp'], tpa=data['tpa'], tpm=data['tpm'], tpp=data['tpp'])
    db.session.add(player)
    db.session.commit()
    return jsonify({'message': 'Player basic prev pctls added'})


# delete basic prev pctls


@player_basic.route('/player/basic_prev_pctls/<string:player_id>', methods=['DELETE'])
@cross_origin()
def delete_player_basic_prev_pctls(player_id):
    player = PlayerBasicPrevPctlModel.query.filter_by(id=player_id).first()
    if not player:
        abort(404, message="Player with that id doesn't exist...")
    db.session.delete(player)
    db.session.commit()
    return jsonify({'message': 'Player basic prev pctls deleted'})

# post player basic stats by year


@player_basic.route('/player/basic_stats/<string:player_id>/<string:year>', methods=['POST'])
@cross_origin()
def post_player_basic_stats_by_year(player_id, year):
    data = request.get_json()
    player = PlayerBasicSeason(player_id=player_id, season=year, mpg=data['mpg'], games_played=data['games_played'], games_started=data['games_started'], ppg=data['ppg'], apg=data['apg'], rpg=data['rpg'], spg=data['spg'],
                               bpg=data['bpg'], topg=data['topg'], pfpg=data['pfpg'], fta=data['fta'], ftm=data['ftm'], ftp=data['ftp'], fga=data['fga'], fgm=data['fgm'], fgp=data['fgp'], tpa=data['tpa'], tpm=data['tpm'], tpp=data['tpp'])
    db.session.add(player)
    db.session.commit()
    return jsonify({'message': 'Player basic stats added'})

# delete player basic stats by year


@player_basic.route('/player/basic_stats/<string:player_id>/<string:year>', methods=['DELETE'])
@cross_origin()
def delete_player_basic_stats_by_year(player_id, year):
    player = PlayerBasicSeason.query.filter_by(
        player_id=player_id, season=year).first()
    if not player:
        abort(404, message="Player basic stats with that id and year doesn't exist...")
    db.session.delete(player)
    db.session.commit()
    return jsonify({'message': 'Player basic stats deleted'})
