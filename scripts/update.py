from player_basic_info import player_bbr_id, player_info
from player_basic_stats import player_basic_latest, player_basic_latest_pctl, player_basic_prev, player_basic_prev_pctl, player_basic_season, player_basic_career
from player_advanced_stats import player_advanced_latest, player_advanced_latest_pctl, player_advanced_prev, player_advanced_prev_pctl, player_advanced_season, player_advanced_career
from player_analysis import average_latest_stats, featured_players, featured_trending_players, future_perf, is_6moy, is_dpoy, is_mip, is_mvp_cand, is_roy, trending_players
from team_basic_info import team_info, team_standings
from team_basic_stats import team_basic_latest
from team_advanced_stats import team_advanced_latest
from team_analysis import featured_teams


def main():
    # print("Updating player basic info...")
    # player_bbr_id.main()
    # player_info.main()
    # print("Updating player basic stats...")
    # player_basic_latest.main()
    # player_basic_latest_pctl.main()
    # player_basic_prev.main()
    # player_basic_prev_pctl.main()
    # player_basic_career.main()
    # print("Updating player advanced stats...")
    # player_advanced_latest.main()
    # player_advanced_latest_pctl.main()
    # player_advanced_prev.main()
    # player_advanced_prev_pctl.main()
    # player_advanced_career.main()
    # print("Updating player analysis...")
    # average_latest_stats.main()
    # featured_players.main()
    # featured_trending_players.main()
    # future_perf.main_2()
    # is_6moy.main()
    # is_dpoy.main()
    # is_mip.main()
    # is_mvp_cand.main()
    # is_roy.main()
    trending_players.main()
    print("Updating team basic info...")
    team_info.main()
    team_standings.main()
    print("Updating team basic stats...")
    team_basic_latest.main()
    print("Updating team advanced stats...")
    team_advanced_latest.main()
    print("Updating team analysis...")
    featured_teams.main()


if __name__ == "__main__":
    main()
