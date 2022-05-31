"""
Resources (dictionaries/lists of columns)
"""

from flask_restful import Api, Resource, marshal, reqparse, abort, fields, marshal_with

player_bbr_id_columns = {
    'bbr_id': str
}

player_info_columns = {
    'team_id': str,
    'first_name': str,
    'last_name': str,
    'pos_abbr': str,
    'pos_full': str,
    'jersey_number': str,
    'debut_year': str,
    'years_pro': str,
    'height_feet': str,
    'height_inches': str,
    'height_meters': str,
    'weight_pounds': str,
    'weight_kilos': str,
    'draft_team_id': str,
    'draft_year': str,
    'draft_round': str,
    'draft_pick': str,
    'college': str,
    'country': str,
}

team_info_columns = {
    "full_name": str,
    "short_name": str,
    "nickname": str,
    "tricode": str,
    "conference": str,
    "division": str,
    "city": str,
}

player_basic_columns = {
    'mpg': str,
    'games_played': str,
    'games_started': str,
    'ppg': str,
    'apg': str,
    'rpg': str,
    'spg': str,
    'bpg': str,
    'topg': str,
    'pfpg': str,
    'fta': str,
    'ftm': str,
    'ftp': str,
    'fga': str,
    'fgm': str,
    'fgp': str,
    'tpa': str,
    'tpm': str,
    'tpp': str
}

player_advanced_columns = {
    'TS_pctg': str,
    'TPAr': str,
    'FTr': str,
    'ORB_pctg': str,
    'DRB_pctg': str,
    'TRB_pctg': str,
    'AST_pctg': str,
    'STL_pctg': str,
    'BLK_pctg': str,
    'TOV_pctg': str,
    'USG_pctg': str,
    'OWS': str,
    'DWS': str,
    'WS': str,
    'WS_48': str,
    'OBPM': str,
    'DBPM': str,
    'BPM': str,
    'VORP': str,
}

# player put args, update args, resource fields

player_bbr_id_put_args = reqparse.RequestParser()
for arg in player_bbr_id_columns:
    player_bbr_id_put_args.add_argument(
        arg, type=player_bbr_id_columns[arg], help=f"{arg} is required", required=True)

player_bbr_id_update_args = reqparse.RequestParser()
for arg in player_bbr_id_columns:
    player_bbr_id_update_args.add_argument(
        arg, type=player_bbr_id_columns[arg], help=f"{arg} is required")

player_bbr_id_resource_fields = {}
for arg in player_bbr_id_columns:
    if (player_bbr_id_columns[arg] == str):
        player_bbr_id_resource_fields[arg] = fields.String

player_put_args = reqparse.RequestParser()
for arg in player_info_columns:
    player_put_args.add_argument(
        arg, type=player_info_columns[arg], help=f"{arg} is required", required=True)

player_update_args = reqparse.RequestParser()
for arg in player_info_columns:
    player_update_args.add_argument(
        arg, type=player_info_columns[arg], help=f"{arg} is required")

player_resource_fields = {}
for arg in player_info_columns:
    if (player_info_columns[arg] == str):
        player_resource_fields[arg] = fields.String

# team put args, update args, resource fields

team_put_args = reqparse.RequestParser()
for arg in team_info_columns:
    team_put_args.add_argument(
        arg, type=team_info_columns[arg], help=f"{arg} is required", required=True)

team_update_args = reqparse.RequestParser()
for arg in team_info_columns:
    team_update_args.add_argument(
        arg, type=team_info_columns[arg], help=f"{arg} is required")

team_resource_fields = {}
for arg in team_info_columns:
    if (team_info_columns[arg] == str):
        team_resource_fields[arg] = fields.String

# player basic put args, update args, resource fields

player_basic_put_args = reqparse.RequestParser()
for arg in player_basic_columns:
    player_basic_put_args.add_argument(
        arg, type=player_basic_columns[arg], help=f"{arg} is required", required=True)

player_basic_update_args = reqparse.RequestParser()
for arg in player_basic_columns:
    player_basic_update_args.add_argument(
        arg, type=player_basic_columns[arg], help=f"{arg} is required")

player_basic_resource_fields = {}
for arg in player_basic_columns:
    if (player_basic_columns[arg] == str):
        player_basic_resource_fields[arg] = fields.String

# player advanced put args, update args, resource fields

player_advanced_put_args = reqparse.RequestParser()
for arg in player_advanced_columns:
    player_advanced_put_args.add_argument(
        arg, type=player_advanced_columns[arg], help=f"{arg} is required", required=True)

player_advanced_update_args = reqparse.RequestParser()
for arg in player_advanced_columns:
    player_advanced_update_args.add_argument(
        arg, type=player_advanced_columns[arg], help=f"{arg} is required")

player_advanced_resource_fields = {}
for arg in player_advanced_columns:
    if (player_advanced_columns[arg] == str):
        player_advanced_resource_fields[arg] = fields.String
