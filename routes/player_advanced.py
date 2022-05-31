from flask import Blueprint, jsonify, request
from flask_cors import CORS, cross_origin
from flask_restful import Api, Resource, marshal, reqparse, abort, fields, marshal_with
from model.models import db, PlayerAdvancedLatestModel, PlayerAdvancedCareerModel, PlayerAdvancedLatestPctlModel, PlayerAdvancedPrevModel, PlayerAdvancedPrevPctlModel, PlayerAdvancedSeason

player_advanced = Blueprint('player_advanced', __name__)

# delete player advanced latest


@player_advanced.route('/player/advanced_latest/<string:player_id>', methods=['DELETE'])
@cross_origin()
def delete_player_advanced_latest(player_id):
    player = PlayerAdvancedLatestModel.query.filter_by(id=player_id).first()
    if not player:
        abort(404, message="Player with that id doesn't exist...")
    db.session.delete(player)
    db.session.commit()
    return jsonify({'message': 'Player advanced latest deleted'})

# post player advanced latest


@player_advanced.route('/player/advanced_latest/<string:player_id>', methods=['POST'])
@cross_origin()
def post_player_advanced_latest(player_id):
    data = request.get_json()
    player = PlayerAdvancedLatestModel(id=player_id, TS_pctg=data['TS_pctg'], TPAr=data['TPAr'], FTr=data['FTr'], ORB_pctg=data['ORB_pctg'], DRB_pctg=data['DRB_pctg'], TRB_pctg=data['TRB_pctg'], AST_pctg=data['AST_pctg'], STL_pctg=data['STL_pctg'],
                                       BLK_pctg=data['BLK_pctg'], TOV_pctg=data['TOV_pctg'], USG_pctg=data['USG_pctg'], OWS=data['OWS'], DWS=data['DWS'], WS=data['WS'], WS_48=data['WS_48'], OBPM=data['OBPM'], DBPM=data['DBPM'], BPM=data['BPM'], VORP=data['VORP'])
    db.session.add(player)
    db.session.commit()
    return jsonify({'message': 'Player advanced latest added'})


# delete player advanced career


@player_advanced.route('/player/advanced_career/<string:player_id>', methods=['DELETE'])
@cross_origin()
def delete_player_advanced_career(player_id):
    player = PlayerAdvancedCareerModel.query.filter_by(id=player_id).first()
    if not player:
        abort(404, message="Player with that id doesn't exist...")
    db.session.delete(player)
    db.session.commit()
    return jsonify({'message': 'Player advanced career deleted'})

# post player advanced career


@player_advanced.route('/player/advanced_career/<string:player_id>', methods=['POST'])
@cross_origin()
def post_player_advanced_career(player_id):
    data = request.get_json()
    player = PlayerAdvancedCareerModel(id=player_id, TS_pctg=data['TS_pctg'], TPAr=data['TPAr'], FTr=data['FTr'], ORB_pctg=data['ORB_pctg'], DRB_pctg=data['DRB_pctg'], TRB_pctg=data['TRB_pctg'], AST_pctg=data['AST_pctg'], STL_pctg=data['STL_pctg'],
                                       BLK_pctg=data['BLK_pctg'], TOV_pctg=data['TOV_pctg'], USG_pctg=data['USG_pctg'], OWS=data['OWS'], DWS=data['DWS'], WS=data['WS'], WS_48=data['WS_48'], OBPM=data['OBPM'], DBPM=data['DBPM'], BPM=data['BPM'], VORP=data['VORP'])
    db.session.add(player)
    db.session.commit()
    return jsonify({'message': 'Player advanced career added'})

# delete player advanced latest pctls


@player_advanced.route('/player/advanced_latest_pctls/<string:player_id>', methods=['DELETE'])
@cross_origin()
def delete_player_advanced_latest_pctls(player_id):
    player = PlayerAdvancedLatestPctlModel.query.filter_by(
        id=player_id).first()
    if not player:
        abort(404, message="Player with that id doesn't exist...")
    db.session.delete(player)
    db.session.commit()
    return jsonify({'message': 'Player advanced latest pctls deleted'})

# post player advanced latest pctls


@player_advanced.route('/player/advanced_latest_pctls/<string:player_id>', methods=['POST'])
@cross_origin()
def post_player_advanced_latest_pctls(player_id):
    data = request.get_json()
    player = PlayerAdvancedLatestPctlModel(id=player_id, TS_pctg=data['TS_pctg'], TPAr=data['TPAr'], FTr=data['FTr'], ORB_pctg=data['ORB_pctg'], DRB_pctg=data['DRB_pctg'], TRB_pctg=data['TRB_pctg'], AST_pctg=data['AST_pctg'], STL_pctg=data['STL_pctg'],
                                           BLK_pctg=data['BLK_pctg'], TOV_pctg=data['TOV_pctg'], USG_pctg=data['USG_pctg'], OWS=data['OWS'], DWS=data['DWS'], WS=data['WS'], WS_48=data['WS_48'], OBPM=data['OBPM'], DBPM=data['DBPM'], BPM=data['BPM'], VORP=data['VORP'])
    db.session.add(player)
    db.session.commit()
    return jsonify({'message': 'Player advanced latest pctls added'})

# post advanced prev stats


@player_advanced.route('/player/advanced_prev_stats/<string:player_id>', methods=['POST'])
@cross_origin()
def post_player_advanced_prev_stats(player_id):
    data = request.get_json()
    player = PlayerAdvancedPrevModel(id=player_id, TS_pctg=data['TS_pctg'], TPAr=data['TPAr'], FTr=data['FTr'], ORB_pctg=data['ORB_pctg'], DRB_pctg=data['DRB_pctg'], TRB_pctg=data['TRB_pctg'], AST_pctg=data['AST_pctg'], STL_pctg=data['STL_pctg'],
                                     BLK_pctg=data['BLK_pctg'], TOV_pctg=data['TOV_pctg'], USG_pctg=data['USG_pctg'], OWS=data['OWS'], DWS=data['DWS'], WS=data['WS'], WS_48=data['WS_48'], OBPM=data['OBPM'], DBPM=data['DBPM'], BPM=data['BPM'], VORP=data['VORP'])
    db.session.add(player)
    db.session.commit()
    return jsonify({'message': 'Player advanced prev stats added'})

# delete advanced prev stats


@player_advanced.route('/player/advanced_prev_stats/<string:player_id>', methods=['DELETE'])
@cross_origin()
def delete_player_advanced_prev_stats(player_id):
    player = PlayerAdvancedPrevModel.query.filter_by(id=player_id).first()
    if not player:
        abort(404, message="Player with that id doesn't exist...")
    db.session.delete(player)
    db.session.commit()
    return jsonify({'message': 'Player advanced prev stats deleted'})

# post advanced prev pctls


@player_advanced.route('/player/advanced_prev_pctls/<string:player_id>', methods=['POST'])
@cross_origin()
def post_player_advanced_prev_pctls(player_id):
    data = request.get_json()
    player = PlayerAdvancedPrevPctlModel(id=player_id, TS_pctg=data['TS_pctg'], TPAr=data['TPAr'], FTr=data['FTr'], ORB_pctg=data['ORB_pctg'], DRB_pctg=data['DRB_pctg'], TRB_pctg=data['TRB_pctg'], AST_pctg=data['AST_pctg'], STL_pctg=data['STL_pctg'],
                                         BLK_pctg=data['BLK_pctg'], TOV_pctg=data['TOV_pctg'], USG_pctg=data['USG_pctg'], OWS=data['OWS'], DWS=data['DWS'], WS=data['WS'], WS_48=data['WS_48'], OBPM=data['OBPM'], DBPM=data['DBPM'], BPM=data['BPM'], VORP=data['VORP'])
    db.session.add(player)
    db.session.commit()
    return jsonify({'message': 'Player advanced prev pctls added'})


# delete advanced prev pctls


@player_advanced.route('/player/advanced_prev_pctls/<string:player_id>', methods=['DELETE'])
@cross_origin()
def delete_player_advanced_prev_pctls(player_id):
    player = PlayerAdvancedPrevPctlModel.query.filter_by(id=player_id).first()
    if not player:
        abort(404, message="Player with that id doesn't exist...")
    db.session.delete(player)
    db.session.commit()
    return jsonify({'message': 'Player advanced prev pctls deleted'})

# post player advanced stats by year


@player_advanced.route('/player/advanced_stats/<string:player_id>/<string:year>', methods=['POST'])
@cross_origin()
def post_player_advanced_stats_by_year(player_id, year):
    data = request.get_json()
    player = PlayerAdvancedSeason(player_id=player_id, season=year, TS_pctg=data['TS_pctg'], TPAr=data['TPAr'], FTr=data['FTr'], ORB_pctg=data['ORB_pctg'], DRB_pctg=data['DRB_pctg'], TRB_pctg=data['TRB_pctg'], AST_pctg=data['AST_pctg'], STL_pctg=data['STL_pctg'],
                                  BLK_pctg=data['BLK_pctg'], TOV_pctg=data['TOV_pctg'], USG_pctg=data['USG_pctg'], OWS=data['OWS'], DWS=data['DWS'], WS=data['WS'], WS_48=data['WS_48'], OBPM=data['OBPM'], DBPM=data['DBPM'], BPM=data['BPM'], VORP=data['VORP'])
    db.session.add(player)
    db.session.commit()
    return jsonify({'message': 'Player advanced stats added'})

# delete player advanced stats by year


@player_advanced.route('/player/advanced_stats/<string:player_id>/<string:year>', methods=['DELETE'])
@cross_origin()
def delete_player_advanced_stats_by_year(player_id, year):
    player = PlayerAdvancedSeason.query.filter_by(
        player_id=player_id, season=year).first()
    if not player:
        abort(404, message="Player advanced stats with that id and year doesn't exist...")
    db.session.delete(player)
    db.session.commit()
    return jsonify({'message': 'Player advanced stats deleted'})
