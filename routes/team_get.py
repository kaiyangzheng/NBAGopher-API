from flask import Blueprint, jsonify, request
from flask_cors import CORS, cross_origin
from flask_restful import Api, Resource, marshal, reqparse, abort, fields, marshal_with
from model.models import db, TeamBasicLatestStats, TeamBasicLatestStatsRankings, TeamAdvancedLatestStats, TeamAdvancedStatsRankings, TeamInfo, TeamStandings

team_get = Blueprint('team_get', __name__)

# get all team basic latest stats


@team_get.route('/team/stats/basic/all', methods=['GET'])
@cross_origin()
def get_all_teams_basic_latest():
    teams = TeamInfo.query.all()

    if not teams:
        abort(404, message="No teams found...")

    basic_latest_data = {}
    for team in teams:
        data = {}
        team_id = team.id
        basic_latest = TeamBasicLatestStats.query.filter_by(
            id=team_id).first()

        if not basic_latest:
            continue

        basic_rankings = TeamBasicLatestStatsRankings.query.filter_by(
            id=team_id).first()

        if not basic_rankings:
            continue

        data['basic'] = {}
        data['basic_rankings'] = {}

        for key, value in basic_latest.__dict__.items():
            if key != '_sa_instance_state':
                data['basic'][key] = value

        for key, value in basic_rankings.__dict__.items():
            if key != '_sa_instance_state':
                data['basic_rankings'][key] = value

        basic_latest_data[team_id] = data

    return jsonify(basic_latest_data)


# get all team advanced latest stats


@team_get.route('/team/stats/advanced/all', methods=['GET'])
@cross_origin()
def get_all_teams_advanced_latest():
    teams = TeamInfo.query.all()

    if not teams:
        abort(404, message="No teams found...")

    advanced_latest_data = {}
    for team in teams:
        data = {}
        team_id = team.id
        advanced_latest = TeamAdvancedLatestStats.query.filter_by(
            id=team_id).first()

        if not advanced_latest:
            continue

        advanced_rankings = TeamAdvancedStatsRankings.query.filter_by(
            id=team_id).first()

        if not advanced_latest:
            continue

        data['advanced'] = {}
        data['advanced_rankings'] = {}

        for key, value in advanced_latest.__dict__.items():
            if key != '_sa_instance_state':
                data['advanced'][key] = value

        for key, value in advanced_rankings.__dict__.items():
            if key != '_sa_instance_state':
                data['advanced_rankings'][key] = value

        advanced_latest_data[team_id] = data
    return jsonify(advanced_latest_data)


# get team basic latest stats


@team_get.route('/team/stats/basic/<string:team_id>', methods=['GET'])
@cross_origin()
def get_team_basic_latest(team_id):
    team = TeamInfo.query.filter_by(id=team_id).first()
    if not team:
        return jsonify({'message': 'Team with that id doesn\'t exist...'})

    basic = TeamBasicLatestStats.query.filter_by(id=team_id).first()
    if not basic:
        return jsonify({'message': 'Team with that id doesn\'t exist...'})

    basic_rankings = TeamBasicLatestStatsRankings.query.filter_by(
        id=team_id).first()
    if not basic_rankings:
        return jsonify({'message': 'Team with that id doesn\'t exist...'})

    team_data = {}
    team_data['basic'] = {}

    for key in basic.__dict__:
        if key != '_sa_instance_state':
            team_data['basic'][key] = basic.__dict__[key]

    team_data['basic_rankings'] = {}

    for key in basic_rankings.__dict__:
        if key != '_sa_instance_state':
            team_data['basic_rankings'][key] = basic_rankings.__dict__[key]

    team_data['info'] = {}

    for key in team.__dict__:
        if key != '_sa_instance_state':
            team_data['info'][key] = team.__dict__[key]

    return jsonify(team_data)


# get team advanced latest stats

@team_get.route('/team/stats/advanced/<string:team_id>', methods=['GET'])
@cross_origin()
def get_team_advanced_latest(team_id):
    team = TeamInfo.query.filter_by(id=team_id).first()
    if not team:
        return jsonify({'message': 'Team with that id doesn\'t exist...'})

    advanced = TeamAdvancedLatestStats.query.filter_by(id=team_id).first()
    if not advanced:
        return jsonify({'message': 'Team with that id doesn\'t exist...'})

    advanced_rankings = TeamAdvancedStatsRankings.query.filter_by(
        id=team_id).first()
    if not advanced_rankings:
        return jsonify({'message': 'Team with that id doesn\'t exist...'})

    team_data = {}
    team_data['info'] = {}

    for key in team.__dict__:
        if key != '_sa_instance_state':
            team_data['info'][key] = team.__dict__[key]

    team_data['advanced'] = {}

    for key in advanced.__dict__:
        if key != '_sa_instance_state':
            team_data['advanced'][key] = advanced.__dict__[key]

    team_data['advanced_rankings'] = {}

    for key in advanced_rankings.__dict__:
        if key != '_sa_instance_state':
            team_data['advanced_rankings'][key] = advanced_rankings.__dict__[key]

    return jsonify(team_data)


# get team compiled stats

@team_get.route('/team/stats/compiled/<string:team_id>', methods=['GET'])
@cross_origin()
def get_team_compiled_stats(team_id):
    team = TeamInfo.query.filter_by(id=team_id).first()

    if not team:
        return jsonify({'message': 'Team with that id doesn\'t exist...'})

    basic = TeamBasicLatestStats.query.filter_by(id=team_id).first()
    basic_rankings = TeamBasicLatestStatsRankings.query.filter_by(
        id=team_id).first()

    advanced = TeamAdvancedLatestStats.query.filter_by(id=team_id).first()
    advanced_rankings = TeamAdvancedStatsRankings.query.filter_by(
        id=team_id).first()

    standings = TeamStandings.query.filter_by(id=team_id).first()

    team_data = {}
    team_data['info'] = {}

    for key in team.__dict__:
        if key != '_sa_instance_state':
            team_data['info'][key] = team.__dict__[key]

    team_data['basic'] = {}

    for key in basic.__dict__:
        if key != '_sa_instance_state':
            team_data['basic'][key] = basic.__dict__[key]

    team_data['basic_rankings'] = {}

    for key in basic_rankings.__dict__:
        if key != '_sa_instance_state':
            team_data['basic_rankings'][key] = basic_rankings.__dict__[key]

    team_data['advanced'] = {}

    for key in advanced.__dict__:
        if key != '_sa_instance_state':
            team_data['advanced'][key] = advanced.__dict__[key]

    team_data['advanced_rankings'] = {}

    for key in advanced_rankings.__dict__:
        if key != '_sa_instance_state':
            team_data['advanced_rankings'][key] = advanced_rankings.__dict__[key]

    team_data['standings'] = {}

    for key in standings.__dict__:
        if key != '_sa_instance_state':
            team_data['standings'][key] = standings.__dict__[key]

    return jsonify(team_data)
