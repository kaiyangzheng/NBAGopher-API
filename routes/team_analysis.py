from flask import Blueprint, jsonify, request
from flask_cors import CORS, cross_origin
from flask_restful import abort
from model.models import db, FeaturedTeams

team_analysis = Blueprint('team_analysis', __name__)

# post featured teams


@team_analysis.route('/featured_teams', method=['POST'])
@cross_origin()
def post_featured_teams():
    data = request.get_json()
    featured_teams = FeaturedTeams(featured_offense_id=data['featured_offense_id'],
                                   featured_defense_id=data['featured_defense_id'], featured_overall_id=data['featured_overall_id'])
    db.session.add(featured_teams)
    db.session.commit()
    return jsonify({'message': 'Featured Teams added successfully!'})


# get featured teams


@team_analysis.route('/featured_teams', method=['GET'])
@cross_origin()
def get_featured_teams():
    featured_teams = FeaturedTeams.query.all()
    featured_teams = featured_teams[-1]
    featured_teams_dict = {}
    featured_teams_dict['featured_offense_id'] = featured_teams.featured_offense_id
    featured_teams_dict['featured_defense_id'] = featured_teams.featured_defense_id
    featured_teams_dict['featured_overall_id'] = featured_teams.featured_overall_id
    return jsonify(featured_teams_dict)
