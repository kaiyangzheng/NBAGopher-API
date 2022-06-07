from flask import Blueprint, jsonify, request
from flask_cors import CORS, cross_origin
from flask_restful import Api, Resource, marshal, reqparse, abort, fields, marshal_with
from model.models import db, WestFirstRound1, WestFirstRound2, WestFirstRound3, WestFirstRound4, EastFirstRound1, EastFirstRound2, EastFirstRound3, EastFirstRound4, WestSemiFinal1, WestSemiFinal2, EastSemiFinal1, EastSemiFinal2, WestConferenceFinal, EastConferenceFinal, NBAFinals

team_playoffs = Blueprint('team_playoffs', __name__)

# post West First Round Info


@team_playoffs.route('/team/playoffs/west/first', methods=['POST'])
@cross_origin()
def post_west_first_round():
    data = request.get_json()
    west_first_round_1 = data[0]
    west_first_round_2 = data[1]
    west_first_round_3 = data[2]
    west_first_round_4 = data[3]

    west_first_round_1_obj = WestFirstRound1(team1_id=west_first_round_1['team1_id'], team2_id=west_first_round_1[
                                             'team2_id'], team1_wins=west_first_round_1['team1_wins'], team2_wins=west_first_round_1['team2_wins'])
    west_first_round_2_obj = WestFirstRound2(team1_id=west_first_round_2['team1_id'], team2_id=west_first_round_2[
                                             'team2_id'], team1_wins=west_first_round_2['team1_wins'], team2_wins=west_first_round_2['team2_wins'])
    west_first_round_3_obj = WestFirstRound3(team1_id=west_first_round_3['team1_id'], team2_id=west_first_round_3[
                                             'team2_id'], team1_wins=west_first_round_3['team1_wins'], team2_wins=west_first_round_3['team2_wins'])
    west_first_round_4_obj = WestFirstRound4(team1_id=west_first_round_4['team1_id'], team2_id=west_first_round_4[
                                             'team2_id'], team1_wins=west_first_round_4['team1_wins'], team2_wins=west_first_round_4['team2_wins'])

    db.session.add(west_first_round_1_obj)
    db.session.add(west_first_round_2_obj)
    db.session.add(west_first_round_3_obj)
    db.session.add(west_first_round_4_obj)
    db.session.commit()
    return jsonify({'message': 'West First Round Info added'})


# post East First Round Info

@team_playoffs.route('/team/playoffs/east/first', methods=['POST'])
@cross_origin()
def post_east_first_round():
    data = request.get_json()
    east_first_round_1 = data[0]
    east_first_round_2 = data[1]
    east_first_round_3 = data[2]
    east_first_round_4 = data[3]

    east_first_round_1_obj = EastFirstRound1(team1_id=east_first_round_1['team1_id'], team2_id=east_first_round_1[
        'team2_id'], team1_wins=east_first_round_1['team1_wins'], team2_wins=east_first_round_1['team2_wins'])
    east_first_round_2_obj = EastFirstRound2(team1_id=east_first_round_2['team1_id'], team2_id=east_first_round_2[
        'team2_id'], team1_wins=east_first_round_2['team1_wins'], team2_wins=east_first_round_2['team2_wins'])
    east_first_round_3_obj = EastFirstRound3(team1_id=east_first_round_3['team1_id'], team2_id=east_first_round_3[
        'team2_id'], team1_wins=east_first_round_3['team1_wins'], team2_wins=east_first_round_3['team2_wins'])
    east_first_round_4_obj = EastFirstRound4(team1_id=east_first_round_4['team1_id'], team2_id=east_first_round_4[
        'team2_id'], team1_wins=east_first_round_4['team1_wins'], team2_wins=east_first_round_4['team2_wins'])

    db.session.add(east_first_round_1_obj)
    db.session.add(east_first_round_2_obj)
    db.session.add(east_first_round_3_obj)
    db.session.add(east_first_round_4_obj)
    return jsonify({'message': 'East First Round Info added'})


# post West Semi Final Info

@team_playoffs.route('/team/playoffs/west/semi', methods=['POST'])
@cross_origin()
def post_west_semi_final():
    data = request.get_json()
    west_semi_final_1 = data[0]
    west_semi_final_2 = data[1]

    west_semi_final_1_obj = WestSemiFinal1(team1_id=west_semi_final_1['team1_id'], team2_id=west_semi_final_1[
        'team2_id'], team1_wins=west_semi_final_1['team1_wins'], team2_wins=west_semi_final_1['team2_wins'])
    west_semi_final_2_obj = WestSemiFinal2(team1_id=west_semi_final_2['team1_id'], team2_id=west_semi_final_2[
        'team2_id'], team1_wins=west_semi_final_2['team1_wins'], team2_wins=west_semi_final_2['team2_wins'])

    db.session.add(west_semi_final_1_obj)
    db.session.add(west_semi_final_2_obj)

    db.session.commit()
    return jsonify({'message': 'West Semi Final Info added'})

# post East Semi Final Info


@team_playoffs.route('/team/playoffs/east/semi', methods=['POST'])
@cross_origin()
def post_east_semi_final():
    data = request.get_json()
    east_semi_final_1 = data[0]
    east_semi_final_2 = data[1]

    east_semi_final_1_obj = EastSemiFinal1(team1_id=east_semi_final_1['team1_id'], team2_id=east_semi_final_1[
        'team2_id'], team1_wins=east_semi_final_1['team1_wins'], team2_wins=east_semi_final_1['team2_wins'])
    east_semi_final_2_obj = EastSemiFinal2(team1_id=east_semi_final_2['team1_id'], team2_id=east_semi_final_2[
        'team2_id'], team1_wins=east_semi_final_2['team1_wins'], team2_wins=east_semi_final_2['team2_wins'])

    db.session.add(east_semi_final_1_obj)
    db.session.add(east_semi_final_2_obj)

    db.session.commit()
    return jsonify({'message': 'East Semi Final Info added'})


# post West Final Info

@team_playoffs.route('/team/playoffs/west/final', methods=['POST'])
@cross_origin()
def post_west_final():
    data = request.get_json()
    west_final = data[0]

    west_final_obj = WestConferenceFinal(team1_id=west_final['team1_id'], team2_id=west_final['team2_id'],
                                         team1_wins=west_final['team1_wins'], team2_wins=west_final['team2_wins'])

    db.session.add(west_final_obj)
    db.session.commit()
    return jsonify({'message': 'West Final Info added'})


# post East Final Info

@team_playoffs.route('/team/playoffs/east/final', methods=['POST'])
@cross_origin()
def post_east_final():
    data = request.get_json()
    east_final = data[0]

    east_final_obj = EastConferenceFinal(team1_id=east_final['team1_id'], team2_id=east_final['team2_id'],
                                         team1_wins=east_final['team1_wins'], team2_wins=east_final['team2_wins'])

    db.session.add(east_final_obj)
    db.session.commit()
    return jsonify({'message': 'East Final Info added'})


# post NBA Final Info

@team_playoffs.route('/team/playoffs/nba/final', methods=['POST'])
@cross_origin()
def post_nba_final():
    data = request.get_json()
    nba_final = data[0]

    nba_final_obj = NBAFinals(team1_id=nba_final['team1_id'], team2_id=nba_final['team2_id'],
                              team1_wins=nba_final['team1_wins'], team2_wins=nba_final['team2_wins'])

    db.session.add(nba_final_obj)
    db.session.commit()
    return jsonify({'message': 'NBA Final Info added'})


# get Playoffs Info

@team_playoffs.route('/team/playoffs/info', methods=['GET'])
@cross_origin()
def get_playoffs_info():
    data = {}

    data['west_first_round'] = {}
    data['east_first_round'] = {}
    data['west_semis'] = {}
    data['west_semis'] = {}
    data['west_finals'] = {}
    data['east_finals'] = {}
    data['nba_finals'] = {}

    data['west_first_round']['series_1'] = {}

    west_first_round1 = WestFirstRound1.query.all()
    west_first_round1 = west_first_round1[-1]

    for key, value in west_first_round1.__dict__.items():
        if key != '_sa_instance_state':
            data['west_first_round']['series_1'][key] = value

    data['west_first_round']['series_2'] = {}

    west_first_round2 = WestFirstRound2.query.all()
    west_first_round2 = west_first_round2[-1]

    for key, value in west_first_round2.__dict__.items():
        if key != '_sa_instance_state':
            data['west_first_round']['series_2'][key] = value

    data['west_first_round']['series_3'] = {}

    west_first_round3 = WestFirstRound3.query.all()
    west_first_round3 = west_first_round3[-1]

    for key, value in west_first_round3.__dict__.items():
        if key != '_sa_instance_state':
            data['west_first_round']['series_3'][key] = value

    west_first_round4 = WestFirstRound4.query.all()
    west_first_round4 = west_first_round4[-1]

    for key, value in west_first_round4.__dict__.items():
        if key != '_sa_instance_state':
            data['west_first_round']['series_4'][key] = value

    data['east_first_round']['series_1'] = {}

    east_first_round1 = EastFirstRound1.query.all()
    east_first_round1 = east_first_round1[-1]

    for key, value in east_first_round1.__dict__.items():
        if key != '_sa_instance_state':
            data['east_first_round']['series_1'][key] = value

    data['east_first_round']['series_2'] = {}

    east_first_round2 = EastFirstRound2.query.all()
    east_first_round2 = east_first_round2[-1]

    for key, value in east_first_round2.__dict__.items():
        if key != '_sa_instance_state':
            data['east_first_round']['series_2'][key] = value

    data['east_first_round']['series_3'] = {}

    east_first_round3 = EastFirstRound3.query.all()
    east_first_round3 = east_first_round3[-1]

    for key, value in east_first_round3.__dict__.items():
        if key != '_sa_instance_state':
            data['east_first_round']['series_3'][key] = value

    east_first_round4 = EastFirstRound4.query.all()
    east_first_round4 = east_first_round4[-1]

    for key, value in east_first_round4.__dict__.items():
        if key != '_sa_instance_state':
            data['east_first_round']['series_4'][key] = value

    data['west_semis']['series_1'] = {}

    west_semi1 = WestSemiFinal1.query.all()
    west_semi1 = west_semi1[-1]

    for key, value in west_semi1.__dict__.items():
        if key != '_sa_instance_state':
            data['west_semis']['series_1'][key] = value

    data['west_semis']['series_2'] = {}

    west_semi2 = WestSemiFinal2.query.all()
    west_semi2 = west_semi2[-1]

    for key, value in west_semi2.__dict__.items():
        if key != '_sa_instance_state':
            data['west_semis']['series_2'][key] = value

    data['east_semis']['series_1'] = {}

    east_semi1 = EastSemiFinal1.query.all()
    east_semi1 = east_semi1[-1]

    for key, value in east_semi1.__dict__.items():
        if key != '_sa_instance_state':
            data['east_semis']['series_1'][key] = value

    data['east_semis']['series_2'] = {}

    east_semi2 = EastSemiFinal2.query.all()
    east_semi2 = east_semi2[-1]

    for key, value in east_semi2.__dict__.items():
        if key != '_sa_instance_state':
            data['east_semis']['series_2'][key] = value

    data['west_finals']['series'] = {}

    west_finals = WestConferenceFinal.query.all()
    west_finals = west_finals[-1]

    for key, value in west_finals.__dict__.items():
        if key != '_sa_instance_state':
            data['west_finals']['series'][key] = value

    data['east_finals']['series'] = {}

    east_finals = EastConferenceFinal.query.all()
    east_finals = east_finals[-1]

    for key, value in east_finals.__dict__.items():
        if key != '_sa_instance_state':
            data['east_finals']['series'][key] = value

    data['nba_finals']['series'] = {}

    nba_finals = NBAFinals.query.all()
    nba_finals = nba_finals[-1]

    for key, value in nba_finals.__dict__.items():
        if key != '_sa_instance_state':
            data['nba_finals']['series'][key] = value

    return jsonify(data)
