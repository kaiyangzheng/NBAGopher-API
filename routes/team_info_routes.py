from flask import Blueprint, jsonify, request
from flask_cors import CORS, cross_origin
from flask_restful import Api, Resource, marshal, reqparse, abort, fields, marshal_with
from model.models import db, TeamInfo, TeamStandings

team_info = Blueprint('team_info', __name__)

# delete team basic info


@team_info.route('/team/info/<string:team_id>', methods=['DELETE'])
@cross_origin()
def delete_team_info(team_id):
    team = TeamInfo.query.filter_by(id=team_id).first()
    if not team:
        abort(404, message="Team with that id doesn't exist...")
    db.session.delete(team)
    db.session.commit()
    return jsonify({'message': 'Team info deleted'})


# post team basic info


@team_info.route('/team/info/<string:team_id>', methods=['POST'])
@cross_origin()
def post_team_info(team_id):
    data = request.get_json()
    team = TeamInfo(id=team_id, city=data['city'], name=data['name'],
                    tricode=data['tricode'], conference=data['conference'], division=data['division'])
    db.session.add(team)
    db.session.commit()
    return jsonify({'message': 'Team info added'})


# get team basic info


@team_info.route('/team/info/<string:team_id>', methods=['GET'])
@cross_origin()
def get_team_info(team_id):
    team = TeamInfo.query.filter_by(id=team_id).first()
    if not team:
        return jsonify({'message': 'No team found'})
    return jsonify({'city': team.city, 'name': team.name, 'tricode': team.tricode,
                    'conference': team.conference, 'division': team.division})


# delete team standings


@team_info.route('/team/standings/<string:team_id>', methods=['DELETE'])
@cross_origin()
def delete_team_standings(team_id):
    team = TeamStandings.query.filter_by(id=team_id).first()
    if not team:
        abort(404, message="Team with that id doesn't exist...")
    db.session.delete(team)
    db.session.commit()
    return jsonify({'message': 'Team standings deleted'})


# post team standings


@team_info.route('/team/standings/<string:team_id>', methods=['POST'])
@cross_origin()
def post_team_standings(team_id):
    data = request.get_json()
    team = TeamStandings(id=team_id, wins=data['wins'], losses=data['losses'], win_pctg=data['win_pctg'], loss_pctg=data['loss_pctg'], games_back=data['games_back'], conf_rank=data['conf_rank'], home_wins=data['home_wins'],
                         home_losses=data['home_losses'], away_wins=data['away_wins'], away_losses=data['away_losses'], last_ten_wins=data['last_ten_wins'], last_ten_losses=data['last_ten_losses'], streak=data['streak'])
    db.session.add(team)
    db.session.commit()
    return jsonify({'message': 'Team standings added'})


# get team standings


@team_info.route('/team/standings/<string:team_id>', methods=['GET'])
@cross_origin()
def get_team_standings(team_id):
    team = TeamStandings.query.filter_by(id=team_id).first()
    if not team:
        return jsonify({'message': 'No team found'})
    return jsonify({'wins': team.wins, 'losses': team.losses, 'win_pctg': team.win_pctg, 'loss_pctg': team.loss_pctg, 'games_back': team.games_back, 'conf_rank': team.conf_rank, 'home_wins': team.home_wins,
                    'home_losses': team.home_losses, 'away_wins': team.away_wins, 'away_losses': team.away_losses, 'last_ten_wins': team.last_ten_wins, 'last_ten_losses': team.last_ten_losses, 'streak': team.streak})


# get all team standings


@team_info.route('/team/standings', methods=['GET'])
@cross_origin()
def get_all_team_standings():
    team_standings = TeamStandings.query.all()
    if not team_standings:
        return jsonify({'message': 'No standings found'})
    standings = {}
    for team in team_standings:
        standings[team.id] = {'wins': team.wins, 'losses': team.losses, 'win_pctg': team.win_pctg, 'loss_pctg': team.loss_pctg, 'games_back': team.games_back, 'conf_rank': team.conf_rank, 'home_wins': team.home_wins,
                              'home_losses': team.home_losses, 'away_wins': team.away_wins, 'away_losses': team.away_losses, 'last_ten_wins': team.last_ten_wins, 'last_ten_losses': team.last_ten_losses, 'streak': team.streak}
    return jsonify(standings)


# get all team info

@team_info.route('/team/info', methods=['GET'])
@cross_origin()
def get_all_team_info():
    team_info = TeamInfo.query.all()
    if not team_info:
        return jsonify({'message': 'No team info found'})
    info = {}
    for team in team_info:
        info[team.id] = {'city': team.city, 'name': team.name, 'tricode': team.tricode,
                         'conference': team.conference, 'division': team.division}
    return jsonify(info)
