from flask import Blueprint, jsonify, request
from flask_cors import CORS, cross_origin
from flask_restful import Api, Resource, marshal, reqparse, abort, fields, marshal_with
from model.models import db, FeaturedPlayers, MVPCandidate, TrendingPlayer, FeaturedTrendingPlayers, FuturePerformance, AverageAdvancedLatestStatsTop30PPG, AverageBasicLatestStatsTop30PPG, PredictedDPOY, PredictedMIP, Predicted6MOY, PredictedROY


player_analysis = Blueprint('player_analysis', __name__)

# post featured players


@player_analysis.route('/featured_players', methods=['POST'])
@cross_origin()
def post_featured_players():
    data = request.get_json()
    featured_players = FeaturedPlayers(
        featured_scorer_id=data['featured_scorer_id'], featured_passer_id=data['featured_passer_id'], featured_defender_id=data['featured_defender_id'])
    db.session.add(featured_players)
    db.session.commit()
    return jsonify({'message': 'Featured players added'})

# get featured players


@player_analysis.route('/featured_players', methods=['GET'])
@cross_origin()
def get_featured_players():
    featured_players = FeaturedPlayers.query.all()
    featured_players = featured_players[-1]
    featured_players_dict = {}
    featured_players_dict['featured_scorer_id'] = featured_players.featured_scorer_id
    featured_players_dict['featured_passer_id'] = featured_players.featured_passer_id
    featured_players_dict['featured_defender_id'] = featured_players.featured_defender_id
    response = jsonify(featured_players_dict)
    return response


# post if mvp candidate (0 or 1)

@player_analysis.route('/mvp_candidate/<string:player_id>', methods=['POST'])
@cross_origin()
def post_mvp_candidate(player_id):
    data = request.get_json()
    mvp_candidate = MVPCandidate(
        id=player_id, is_mvp_cand=data['is_mvp_cand'])
    db.session.add(mvp_candidate)
    db.session.commit()
    return jsonify({'message': 'MVP candidate added'})

# delete if mvp candidate (0 or 1)


@player_analysis.route('/mvp_candidate/<string:player_id>', methods=['DELETE'])
@cross_origin()
def delete_mvp_candidate(player_id):
    mvp_candidate = MVPCandidate.query.filter_by(id=player_id).first()
    if not mvp_candidate:
        abort(404, message="MVP candidate with that id doesn't exist...")
    db.session.delete(mvp_candidate)
    db.session.commit()
    return jsonify({'message': 'MVP candidate deleted'})

# get is mvp candidate by player id


@player_analysis.route('/mvp_candidate/<string:player_id>', methods=['GET'])
@cross_origin()
def get_mvp_candidate(player_id):
    mvp_candidate = MVPCandidate.query.filter_by(id=player_id).first()
    if not mvp_candidate:
        abort(404, message="Player with that id doesn't exist...")
    output = {}
    output['is_mvp_cand'] = mvp_candidate.is_mvp_cand
    response = jsonify(output)
    return response

# get all mvp candidates


@player_analysis.route('/mvp_candidates', methods=['GET'])
@cross_origin()
def get_mvp_candidates():
    mvp_candidates = MVPCandidate.query.all()
    mvp_candidates_list = []
    for mvp_candidate in mvp_candidates:
        if (mvp_candidate.is_mvp_cand == 1):
            mvp_candidates_list.append(mvp_candidate.id)
    response = jsonify(mvp_candidates_list)
    return response

# post trending player


@ player_analysis.route('/player/trending_player/<string:player_id>', methods=['POST'])
@ cross_origin()
def post_player_trending_player(player_id):
    data = request.get_json()
    trending_player = TrendingPlayer(
        id=player_id, is_improving=data['is_improving'])
    db.session.add(trending_player)
    db.session.commit()
    return jsonify({'message': 'Trending player added'})

# delete trending player


@ player_analysis.route('/player/trending_player/<string:player_id>', methods=['DELETE'])
@ cross_origin()
def delete_player_trending_player(player_id):
    trending_player = TrendingPlayer.query.filter_by(id=player_id).first()
    if not trending_player:
        abort(404, message="Trending player with that id doesn't exist...")
    db.session.delete(trending_player)
    db.session.commit()
    return jsonify({'message': 'Trending player deleted'})

# get all trending players


@ player_analysis.route('/player/trending_players', methods=['GET'])
@ cross_origin()
def get_player_trending_players():
    trending_players = TrendingPlayer.query.all()
    trending_players_list = []
    for trending_player in trending_players:
        trending_player_data = {}
        trending_player_data['id'] = trending_player.id
        trending_player_data['is_improving'] = trending_player.is_improving
        trending_players_list.append(trending_player_data)
    response = jsonify(trending_players_list)
    return response

# delete all trending players


@ player_analysis.route('/player/trending_players', methods=['DELETE'])
@ cross_origin()
def delete_player_trending_players():
    trending_players = TrendingPlayer.query.all()
    for trending_player in trending_players:
        db.session.delete(trending_player)
    db.session.commit()
    return jsonify({'message': 'Trending players deleted'})

# post featured trending players


@ player_analysis.route('/player/featured_trending_players', methods=['POST'])
@ cross_origin()
def post_featured_trending_players():
    data = request.get_json()
    featured_trending_players = FeaturedTrendingPlayers(featured_offense_improve_id=data['featured_offense_improve_id'], featured_defense_improve_id=data[
        'featured_defense_improve_id'], featured_offense_decline_id=data['featured_offense_decline_id'], featured_defense_decline_id=data['featured_defense_decline_id'])
    db.session.add(featured_trending_players)
    db.session.commit()
    return jsonify({'message': 'Featured trending players added'})

# get featured trending players


@ player_analysis.route('/player/featured_trending_players', methods=['GET'])
@ cross_origin()
def get_featured_trending_players():
    featured_trending_players = FeaturedTrendingPlayers.query.all()
    featured_trending_players = featured_trending_players[-1]
    featured_trending_players_list = {}
    featured_trending_players_list['featured_offense_improve_id'] = featured_trending_players.featured_offense_improve_id
    featured_trending_players_list['featured_defense_improve_id'] = featured_trending_players.featured_defense_improve_id
    featured_trending_players_list['featured_offense_decline_id'] = featured_trending_players.featured_offense_decline_id
    featured_trending_players_list['featured_defense_decline_id'] = featured_trending_players.featured_defense_decline_id
    response = jsonify(featured_trending_players_list)
    return response


# post future performance

@ player_analysis.route('/player/future_performance/<string:player_id>', methods=['POST'])
@ cross_origin()
def post_future_performance(player_id):
    data = request.get_json()
    future_performance = FuturePerformance(
        id=player_id, mpg=data['mpg'], ppg=data['ppg'], apg=data['apg'], rpg=data['rpg'], TS_pctg=data['TS_pctg'], BPM=data['BPM'])
    db.session.add(future_performance)
    db.session.commit()
    return jsonify({'message': 'Future performance added'})


# delete future performance

@ player_analysis.route('/player/future_performance/<string:player_id>', methods=['DELETE'])
@ cross_origin()
def delete_future_performance(player_id):
    future_performance = FuturePerformance.query.filter_by(
        id=player_id).first()
    if not future_performance:
        abort(404, message="Future performance with that id doesn't exist...")
    db.session.delete(future_performance)
    db.session.commit()
    return jsonify({'message': 'Future performance deleted'})


# post average basic stats (top 30 ppg)

@ player_analysis.route('/player/average_basic_stats_top_30_ppg', methods=['POST'])
@ cross_origin()
def post_average_basic_stats_top_30_ppg():
    data = request.get_json()
    average_basic_stats_top_30_ppg = AverageBasicLatestStatsTop30PPG(mpg=data['mpg'], games_played=data['games_played'], games_started=data[
        'games_started'], ppg=data['ppg'], apg=data['apg'], rpg=data['rpg'], spg=data['spg'],
        bpg=data['bpg'], topg=data['topg'], pfpg=data['pfpg'], fta=data['fta'], ftm=data['ftm'], ftp=data['ftp'], fga=data['fga'], fgm=data['fgm'], fgp=data['fgp'], tpa=data['tpa'], tpm=data['tpm'], tpp=data['tpp'])
    db.session.add(average_basic_stats_top_30_ppg)
    db.session.commit()
    return jsonify({'message': 'Average basic stats top 30 ppg added'})

# post average advanced stats (top 30 ppg)


@ player_analysis.route('/player/average_advanced_stats_top_30_ppg', methods=['POST'])
@ cross_origin()
def post_average_advanced_stats_top_30_ppg():
    data = request.get_json()
    average_advanced_stats_top_30_ppg = AverageAdvancedLatestStatsTop30PPG(TS_pctg=data['TS_pctg'], TPAr=data['TPAr'], FTr=data['FTr'], ORB_pctg=data['ORB_pctg'], DRB_pctg=data['DRB_pctg'], TRB_pctg=data['TRB_pctg'], AST_pctg=data['AST_pctg'], STL_pctg=data['STL_pctg'],
                                                                           BLK_pctg=data['BLK_pctg'], TOV_pctg=data['TOV_pctg'], USG_pctg=data['USG_pctg'], OWS=data['OWS'], DWS=data['DWS'], WS=data['WS'], WS_48=data['WS_48'], OBPM=data['OBPM'], DBPM=data['DBPM'], BPM=data['BPM'], VORP=data['VORP'])
    db.session.add(average_advanced_stats_top_30_ppg)
    db.session.commit()
    return jsonify({'message': 'Average advanced stats top 30 ppg added'})

# get average stats (top 30 ppg)


@ player_analysis.route('/player/average_stats_top_30_ppg', methods=['GET'])
@ cross_origin()
def get_average_stats_top_30_ppg():
    average_basic_stats = AverageBasicLatestStatsTop30PPG.query.all()
    average_basic_stats = average_basic_stats[-1]
    average_advanced_stats = AverageAdvancedLatestStatsTop30PPG.query.all()
    average_advanced_stats = average_advanced_stats[-1]

    average_stats = {}
    average_stats['average_basic_stats'] = {}
    for key in average_basic_stats.__dict__:
        if key != '_sa_instance_state':
            average_stats['average_basic_stats'][key] = average_basic_stats.__dict__[
                key]

    average_stats['average_advanced_stats'] = {}
    for key in average_advanced_stats.__dict__:
        if key != '_sa_instance_state':
            average_stats['average_advanced_stats'][key] = average_advanced_stats.__dict__[
                key]
    response = jsonify(average_stats)
    return response


# post predicted dpoy

@player_analysis.route('/player/predicted_dpoy', methods=['POST'])
@cross_origin()
def post_predicted_dpoy():
    data = request.get_json()
    predicted_dpoy = PredictedDPOY(
        id=data['player'])
    db.session.add(predicted_dpoy)
    db.session.commit()
    return jsonify({'message': 'Predicted dpoy added'})

# get predicted dpoy


@player_analysis.route('/player/predicted_dpoy', methods=['GET'])
@cross_origin()
def get_predicted_dpoy():
    predicted_dpoy = PredictedDPOY.query.all()
    predicted_dpoy = predicted_dpoy[-1]
    response = jsonify({'id': predicted_dpoy.id})
    return response

# post predicted mip


@player_analysis.route('/player/predicted_mip', methods=['POST'])
@cross_origin()
def post_predicted_mip():
    data = request.get_json()
    predicted_mip = PredictedMIP(
        id=data['player'])
    db.session.add(predicted_mip)
    db.session.commit()
    return jsonify({'message': 'Predicted mip added'})


# get predicted mip

@player_analysis.route('/player/predicted_mip', methods=['GET'])
@cross_origin()
def get_predicted_mip():
    predicted_mip = PredictedMIP.query.all()
    predicted_mip = predicted_mip[-1]
    response = jsonify({'id': predicted_mip.id})
    return response


# post predicted 6moy


@player_analysis.route('/player/predicted_6moy', methods=['POST'])
@cross_origin()
def post_predicted_6moy():
    data = request.get_json()
    predicted_6moy = Predicted6MOY(
        id=data['player'])
    db.session.add(predicted_6moy)
    db.session.commit()
    return jsonify({'message': 'Predicted 6moy added'})

# get predicted 6moy


@player_analysis.route('/player/predicted_6moy', methods=['GET'])
@cross_origin()
def get_predicted_6moy():
    predicted_6moy = Predicted6MOY.query.all()
    predicted_6moy = predicted_6moy[-1]
    response = jsonify({'id': predicted_6moy.id})
    return response


# post predicted roy

@player_analysis.route('/player/predicted_roy', methods=['POST'])
@cross_origin()
def post_predicted_roy():
    data = request.get_json()
    predicted_roy = PredictedROY(
        id=data['player'])
    db.session.add(predicted_roy)
    db.session.commit()
    return jsonify({'message': 'Predicted roy added'})


# get predicted roy

@player_analysis.route('/player/predicted_roy', methods=['GET'])
@cross_origin()
def get_predicted_roy():
    predicted_roy = PredictedROY.query.all()
    predicted_roy = predicted_roy[-1]
    response = jsonify({'id': predicted_roy.id})
    return response
