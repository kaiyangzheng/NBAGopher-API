from flask import Blueprint, jsonify, request
from flask_cors import CORS, cross_origin
from flask_restful import Api, Resource, marshal, reqparse, abort, fields, marshal_with
from models import db, PlayerInfoModel, PlayerBasicLatestModel, PlayerAdvancedLatestModel, PlayerBasicCareerModel, PlayerAdvancedCareerModel, PlayerBasicPrevModel, PlayerAdvancedPrevModel, PlayerBasicLatestPctlModel, PlayerAdvancedLatestPctlModel, FuturePerformance, PlayerBasicSeason, PlayerAdvancedSeason, PlayerBasicPrevPctlModel, PlayerAdvancedPrevPctlModel

player_get_stats = Blueprint('player_get_stats', __name__)

# get compiled player stats


@player_get_stats.route('/player/compiled/<string:player_id>', methods=['GET'])
@cross_origin()
def get_player(player_id):
    player = PlayerInfoModel.query.filter_by(id=player_id).first()
    if not player:
        return jsonify({'message': 'No player found'})
    player_basic_latest = PlayerBasicLatestModel.query.filter_by(
        id=player_id).first()
    player_basic_career = PlayerBasicCareerModel.query.filter_by(
        id=player_id).first()
    player_advanced_latest = PlayerAdvancedLatestModel.query.filter_by(
        id=player_id).first()
    player_advanced_career = PlayerAdvancedCareerModel.query.filter_by(
        id=player_id).first()
    player_basic_prev = PlayerBasicPrevModel.query.filter_by(
        id=player_id).first()
    player_advanced_prev = PlayerAdvancedPrevModel.query.filter_by(
        id=player_id).first()
    future_predicted_perf = FuturePerformance.query.filter_by(
        id=player_id).first()
    player_data = {}

    player_data['player_info'] = {}

    if player:
        for key in player.__dict__:
            if key != '_sa_instance_state':
                player_data['player_info'][key] = player.__dict__[key]

    player_data['player_basic_latest'] = {}

    if player_basic_latest:
        for key in player_basic_latest.__dict__:
            if key != '_sa_instance_state':
                player_data['player_basic_latest'][key] = player_basic_latest.__dict__[
                    key]

    player_data['player_basic_career'] = {}

    if player_basic_career:
        for key in player_basic_career.__dict__:
            if key != '_sa_instance_state':
                player_data['player_basic_career'][key] = player_basic_career.__dict__[
                    key]

    player_data['player_advanced_latest'] = {}

    if player_advanced_latest:
        for key in player_advanced_latest.__dict__:
            if key != '_sa_instance_state':
                player_data['player_advanced_latest'][key] = player_advanced_latest.__dict__[
                    key]

    player_data['player_advanced_career'] = {}

    if player_advanced_career:
        for key in player_advanced_career.__dict__:
            if key != '_sa_instance_state':
                player_data['player_advanced_career'][key] = player_advanced_career.__dict__[
                    key]

    player_data['player_basic_prev'] = {}

    if player_basic_prev:
        for key in player_basic_prev.__dict__:
            if key != '_sa_instance_state':
                player_data['player_basic_prev'][key] = player_basic_prev.__dict__[
                    key]

    player_data['player_advanced_prev'] = {}

    if player_advanced_prev:
        for key in player_advanced_prev.__dict__:
            if key != '_sa_instance_state':
                player_data['player_advanced_prev'][key] = player_advanced_prev.__dict__[
                    key]

    player_data['predicted_future_perf'] = {}

    if future_predicted_perf:
        for key in future_predicted_perf.__dict__:
            if key != '_sa_instance_state':
                player_data['predicted_future_perf'][key] = future_predicted_perf.__dict__[
                    key]
    response = jsonify(player_data)
    return response

# get compiled player pctls


@player_get_stats.route('/player/compiled/pctls/<string:player_id>', methods=['GET'])
@cross_origin()
def get_player_pctls(player_id):
    player = PlayerInfoModel.query.filter_by(id=player_id).first()
    if not player:
        return jsonify({'message': 'No player found'})
    player_basic_latest_pctls = PlayerBasicLatestPctlModel.query.filter_by(
        id=player_id).first()
    player_advanced_latest_pctls = PlayerAdvancedLatestPctlModel.query.filter_by(
        id=player_id).first()
    player_basic_prev_pctls = PlayerBasicPrevPctlModel.query.filter_by(
        id=player_id).first()
    player_advanced_prev_pctls = PlayerAdvancedPrevPctlModel.query.filter_by(
        id=player_id).first()

    player_data = {}

    player_data['player_basic_latest_pctls'] = {}
    for key in player_basic_latest_pctls.__dict__:
        if key != '_sa_instance_state':
            player_data['player_basic_latest_pctls'][key] = player_basic_latest_pctls.__dict__[
                key]

    player_data['player_advanced_latest_pctls'] = {}
    for key in player_advanced_latest_pctls.__dict__:
        if key != '_sa_instance_state':
            player_data['player_advanced_latest_pctls'][key] = player_advanced_latest_pctls.__dict__[
                key]

    player_data['player_basic_prev_pctls'] = {}
    try:
        for key in player_basic_prev_pctls.__dict__:
            if key != '_sa_instance_state':
                player_data['player_basic_prev_pctls'][key] = player_basic_prev_pctls.__dict__[
                    key]
    except:
        pass

    player_data['player_advanced_prev_pctls'] = {}
    try:
        for key in player_advanced_prev_pctls.__dict__:
            if key != '_sa_instance_state':
                player_data['player_advanced_prev_pctls'][key] = player_advanced_prev_pctls.__dict__[
                    key]
    except:
        pass

    response = jsonify(player_data)
    return response


# get players stats by year

@player_get_stats.route('/player/compiled/by_season/<string:player_id>', methods=['GET'])
@cross_origin()
def get_player_stats_by_year(player_id):
    player = PlayerInfoModel.query.filter_by(id=player_id).first()
    if not player:
        abort(404, message="Player with that id doesn't exist...")
    player_basic_stats = PlayerBasicSeason.query.filter_by(
        player_id=player_id).all()
    player_advanced_stats = PlayerAdvancedSeason.query.filter_by(
        player_id=player_id).all()
    player_basic_stats_list = []
    player_advanced_stats_list = []
    for stat in player_basic_stats:
        player_basic_stats_data = {}
        for key in stat.__dict__:
            if key != '_sa_instance_state':
                player_basic_stats_data[key] = stat.__dict__[key]
        player_basic_stats_list.append(player_basic_stats_data)
    for stat in player_advanced_stats:
        player_advanced_stats_data = {}
        for key in stat.__dict__:
            if key != '_sa_instance_state':
                player_advanced_stats_data[key] = stat.__dict__[key]
        player_advanced_stats_list.append(player_advanced_stats_data)
    response = jsonify({'player_basic_stats': player_basic_stats_list,
                       'player_advanced_stats': player_advanced_stats_list})
    return response
