from basic_stats import player_basic_career, player_basic_latest_pctl, player_basic_latest, player_basic_prev, player_basic_prev_pctl, player_basic_season
from advanced_stats import player_advanced_career, player_advanced_latest, player_advanced_latest_pctl, player_advanced_prev, player_advanced_prev_pctl, player_advanced_season
from basic_info import player_bbr_id, player_info
from analysis import average_latest_stats, featured_players, featured_trending_players, future_perf, is_6moy, is_dpoy, is_mip, is_mvp_cand, trending_players


def main():
    # Update basic info
    player_bbr_id.main()
    player_info.main()

    # Update basic stats
    player_basic_career.main()
    player_basic_latest_pctl.main()
    player_basic_prev.main()
    player_basic_prev_pctl.main()
    player_basic_season.main()

    # Update advanced stats
    player_advanced_career.main()
    player_advanced_latest_pctl.main()
    player_advanced_latest.main()
    player_advanced_prev.main()
    player_advanced_prev_pctl.main()
    player_advanced_season.main()

    # Update analysis
    average_latest_stats.main()
    featured_players.main()
    featured_trending_players.main()
    future_perf.main()
    is_6moy.main()
    is_dpoy.main()
    is_mip.main()
    is_mvp_cand.main()
    trending_players.main()


if __name__ == '__main__':
    main()
