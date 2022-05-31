from flask import Blueprint, jsonify, request
from flask_cors import CORS, cross_origin
from flask_restful import Api, Resource, marshal, reqparse, abort, fields, marshal_with
from model.models import db, TeamBasicLatestStats, TeamBasicLatestStatsRankings, TeamAdvancedLatestStats, TeamAdvancedStatsRankings, TeamInfo

team_stats = Blueprint('team_stats', __name__)

# delete team basic latest stats


@team_stats.route('/team/stats/basic/<string:team_id>', methods=['DELETE'])
@cross_origin()
def delete_team_stats(team_id):
    team = TeamBasicLatestStats.query.filter_by(id=team_id).first()
    if not team:
        abort(404, message="Team with that id doesn't exist...")
    db.session.delete(team)
    db.session.commit()
    return jsonify({'message': 'Team stats deleted'})


# post team basic latest stats


@team_stats.route('/team/stats/basic/<string:team_id>', methods=['POST'])
@cross_origin()
def post_team_stats(team_id):
    data = request.get_json()
    team = TeamBasicLatestStats(id=team_id, mpg=data['mpg'], fgp=data['fgp'], ftp=data['ftp'], tpp=data['tpp'], orpg=data['orpg'], drpg=data['drpg'],
                                trpg=data['trpg'], apg=data['apg'], spg=data['spg'], bpg=data['bpg'], pfpg=data['pfpg'], ppg=data['ppg'], oopg=data['oopg'], netppg=data['netppg'])
    db.session.add(team)
    db.session.commit()
    return jsonify({'message': 'Team stats posted'})


# delete team basic latest stats rankings


@team_stats.route('/team/stats/basic/rankings/<string:team_id>', methods=['DELETE'])
@cross_origin()
def delete_team_stats_rankings(team_id):
    team = TeamBasicLatestStatsRankings.query.filter_by(id=team_id).first()
    if not team:
        abort(404, message="Team with that id doesn't exist...")
    db.session.delete(team)
    db.session.commit()
    return jsonify({'message': 'Team stats rankings deleted'})


# post team basic latest stats rankings


@team_stats.route('/team/stats/basic/rankings/<string:team_id>', methods=['POST'])
@cross_origin()
def post_team_stats_rankings(team_id):
    data = request.get_json()
    team = TeamBasicLatestStatsRankings(id=team_id, mpg=data['mpg'], fgp=data['fgp'], ftp=data['ftp'], tpp=data['tpp'], orpg=data['orpg'], drpg=data['drpg'],
                                        trpg=data['trpg'], apg=data['apg'], spg=data['spg'], bpg=data['bpg'], pfpg=data['pfpg'], ppg=data['ppg'], oopg=data['oopg'], netppg=data['netppg'])
    db.session.add(team)
    db.session.commit()
    return jsonify({'message': 'Team stats rankings posted'})


# delete team advanced latest stats


@team_stats.route('/team/stats/advanced/<string:team_id>', methods=['DELETE'])
@cross_origin()
def delete_team_stats_advanced(team_id):
    team = TeamAdvancedLatestStats.query.filter_by(id=team_id).first()
    if not team:
        abort(404, message="Team with that id doesn't exist...")
    db.session.delete(team)
    db.session.commit()
    return jsonify({'message': 'Team stats advanced deleted'})


# post team advanced latest stats


@team_stats.route('/team/stats/advanced/<string:team_id>', methods=['POST'])
@cross_origin()
def post_team_stats_advanced(team_id):
    data = request.get_json()
    team = TeamAdvancedLatestStats(id=team_id, ORTG=data['ORTG'], DRTG=data['DRTG'], NRTG=data['NRTG'], Pace=data['Pace'], FTr=data['FTr'], TPAr=data['TPAr'], TS_pctg=data['TS_pctg'], eFG_pctg=data['eFG_pctg'],
                                   TOV_pctg=data['TOV_pctg'], ORB_pctg=data['ORB_pctg'], FT_per_FGA=data['FT_per_FGA'], opp_eFG_pctg=data['opp_eFG_pctg'], opp_TOV_pctg=data['opp_TOV_pctg'], DRB_pctg=data['DRB_pctg'], opp_FT_per_FGA=data['opp_FT_per_FGA'])
    db.session.add(team)
    db.session.commit()
    return jsonify({'message': 'Team stats advanced posted'})


# delete team advanced latest stats rankings


@team_stats.route('/team/stats/advanced/rankings/<string:team_id>', methods=['DELETE'])
@cross_origin()
def delete_team_stats_advanced_rankings(team_id):
    team = TeamAdvancedStatsRankings.query.filter_by(id=team_id).first()
    if not team:
        abort(404, message="Team with that id doesn't exist...")
    db.session.delete(team)
    db.session.commit()
    return jsonify({'message': 'Team stats advanced rankings deleted'})


# post team advanced latest stats rankings


@team_stats.route('/team/stats/advanced/rankings/<string:team_id>', methods=['POST'])
@cross_origin()
def post_team_stats_advanced_rankings(team_id):
    data = request.get_json()
    team = TeamAdvancedStatsRankings(id=team_id, ORTG=data['ORTG'], DRTG=data['DRTG'], NRTG=data['NRTG'], Pace=data['Pace'], FTr=data['FTr'], TPAr=data['TPAr'], TS_pctg=data['TS_pctg'], eFG_pctg=data['eFG_pctg'],
                                     TOV_pctg=data['TOV_pctg'], ORB_pctg=data['ORB_pctg'], FT_per_FGA=data['FT_per_FGA'], opp_eFG_pctg=data['opp_eFG_pctg'], opp_TOV_pctg=data['opp_TOV_pctg'], DRB_pctg=data['DRB_pctg'], opp_FT_per_FGA=data['opp_FT_per_FGA'])
    db.session.add(team)
    db.session.commit()
    return jsonify({'message': 'Team stats advanced rankings posted'})


# get team basic latest stats

@team_stats.route('/team/stats/basic/<string:team_id>', methods=['GET'])
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

@team_stats.route('/team/stats/advanced/<string:team_id>', methods=['GET'])
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
