from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

##############################################################################
# Player Info Models
##############################################################################

# bbref id db


class PlayerBbrIdModel(db.Model):
    id = db.Column(db.String(100), primary_key=True)
    bbr_id = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"PlayerBbrId(bbr_id = {self.bbr_id})"

# player info db


class PlayerInfoModel(db.Model):
    id = db.Column(db.String(100), primary_key=True)
    team_id = db.Column(db.String(100), nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    pos_abbr = db.Column(db.String(100), nullable=False)
    pos_full = db.Column(db.String(100), nullable=False)
    jersey_number = db.Column(db.String(100), nullable=False)
    debut_year = db.Column(db.String(100), nullable=False)
    years_pro = db.Column(db.String(100), nullable=False)
    height_feet = db.Column(db.String(100), nullable=False)
    height_inches = db.Column(db.String(100), nullable=False)
    height_meters = db.Column(db.String(100), nullable=False)
    weight_pounds = db.Column(db.String(100), nullable=False)
    weight_kilos = db.Column(db.String(100), nullable=False)
    draft_team_id = db.Column(db.String(100), nullable=True)
    draft_year = db.Column(db.String(100), nullable=True)
    draft_round = db.Column(db.String(100), nullable=True)
    draft_pick = db.Column(db.String(100), nullable=True)
    college = db.Column(db.String(100), nullable=True)
    country = db.Column(db.String(100), nullable=True)


##############################################################################
# Player Basic Stats Models
##############################################################################

# player basic stats db
class PlayerBasicLatestModel(db.Model):
    id = db.Column(db.String(100), primary_key=True)
    mpg = db.Column(db.String(100), nullable=False)
    games_played = db.Column(db.String(100), nullable=False)
    games_started = db.Column(db.String(100), nullable=False)
    ppg = db.Column(db.String(100), nullable=False)
    apg = db.Column(db.String(100), nullable=False)
    rpg = db.Column(db.String(100), nullable=False)
    spg = db.Column(db.String(100), nullable=False)
    bpg = db.Column(db.String(100), nullable=False)
    topg = db.Column(db.String(100), nullable=False)
    pfpg = db.Column(db.String(100), nullable=False)
    fta = db.Column(db.String(100), nullable=False)
    ftm = db.Column(db.String(100), nullable=False)
    ftp = db.Column(db.String(100), nullable=False)
    fga = db.Column(db.String(100), nullable=False)
    fgm = db.Column(db.String(100), nullable=False)
    fgp = db.Column(db.String(100), nullable=False)
    tpa = db.Column(db.String(100), nullable=False)
    tpm = db.Column(db.String(100), nullable=False)
    tpp = db.Column(db.String(100), nullable=False)

# player basic stats previous year db


class PlayerBasicPrevModel(db.Model):
    id = db.Column(db.String(100), primary_key=True)
    mpg = db.Column(db.String(100), nullable=False)
    games_played = db.Column(db.String(100), nullable=False)
    games_started = db.Column(db.String(100), nullable=False)
    ppg = db.Column(db.String(100), nullable=False)
    apg = db.Column(db.String(100), nullable=False)
    rpg = db.Column(db.String(100), nullable=False)
    spg = db.Column(db.String(100), nullable=False)
    bpg = db.Column(db.String(100), nullable=False)
    topg = db.Column(db.String(100), nullable=False)
    pfpg = db.Column(db.String(100), nullable=False)
    fta = db.Column(db.String(100), nullable=False)
    ftm = db.Column(db.String(100), nullable=False)
    ftp = db.Column(db.String(100), nullable=False)
    fga = db.Column(db.String(100), nullable=False)
    fgm = db.Column(db.String(100), nullable=False)
    fgp = db.Column(db.String(100), nullable=False)
    tpa = db.Column(db.String(100), nullable=False)
    tpm = db.Column(db.String(100), nullable=False)
    tpp = db.Column(db.String(100), nullable=False)

# player basic stat pctls db


class PlayerBasicLatestPctlModel(db.Model):
    id = db.Column(db.String(100), primary_key=True)
    mpg = db.Column(db.String(100), nullable=False)
    games_played = db.Column(db.String(100), nullable=False)
    games_started = db.Column(db.String(100), nullable=False)
    ppg = db.Column(db.String(100), nullable=False)
    apg = db.Column(db.String(100), nullable=False)
    rpg = db.Column(db.String(100), nullable=False)
    spg = db.Column(db.String(100), nullable=False)
    bpg = db.Column(db.String(100), nullable=False)
    topg = db.Column(db.String(100), nullable=False)
    pfpg = db.Column(db.String(100), nullable=False)
    fta = db.Column(db.String(100), nullable=False)
    ftm = db.Column(db.String(100), nullable=False)
    ftp = db.Column(db.String(100), nullable=False)
    fga = db.Column(db.String(100), nullable=False)
    fgm = db.Column(db.String(100), nullable=False)
    fgp = db.Column(db.String(100), nullable=False)
    tpa = db.Column(db.String(100), nullable=False)
    tpm = db.Column(db.String(100), nullable=False)
    tpp = db.Column(db.String(100), nullable=False)

# player stats previous pctls db


class PlayerBasicPrevPctlModel(db.Model):
    id = db.Column(db.String(100), primary_key=True)
    mpg = db.Column(db.String(100), nullable=False)
    games_played = db.Column(db.String(100), nullable=False)
    games_started = db.Column(db.String(100), nullable=False)
    ppg = db.Column(db.String(100), nullable=False)
    apg = db.Column(db.String(100), nullable=False)
    rpg = db.Column(db.String(100), nullable=False)
    spg = db.Column(db.String(100), nullable=False)
    bpg = db.Column(db.String(100), nullable=False)
    topg = db.Column(db.String(100), nullable=False)
    pfpg = db.Column(db.String(100), nullable=False)
    fta = db.Column(db.String(100), nullable=False)
    ftm = db.Column(db.String(100), nullable=False)
    ftp = db.Column(db.String(100), nullable=False)
    fga = db.Column(db.String(100), nullable=False)
    fgm = db.Column(db.String(100), nullable=False)
    fgp = db.Column(db.String(100), nullable=False)
    tpa = db.Column(db.String(100), nullable=False)
    tpm = db.Column(db.String(100), nullable=False)
    tpp = db.Column(db.String(100), nullable=False)

# player basic career summary db


class PlayerBasicCareerModel(db.Model):
    id = db.Column(db.String(100), primary_key=True)
    mpg = db.Column(db.String(100), nullable=False)
    games_played = db.Column(db.String(100), nullable=False)
    games_started = db.Column(db.String(100), nullable=False)
    ppg = db.Column(db.String(100), nullable=False)
    apg = db.Column(db.String(100), nullable=False)
    rpg = db.Column(db.String(100), nullable=False)
    spg = db.Column(db.String(100), nullable=False)
    bpg = db.Column(db.String(100), nullable=False)
    topg = db.Column(db.String(100), nullable=False)
    pfpg = db.Column(db.String(100), nullable=False)
    fta = db.Column(db.String(100), nullable=False)
    ftm = db.Column(db.String(100), nullable=False)
    ftp = db.Column(db.String(100), nullable=False)
    fga = db.Column(db.String(100), nullable=False)
    fgm = db.Column(db.String(100), nullable=False)
    fgp = db.Column(db.String(100), nullable=False)
    tpa = db.Column(db.String(100), nullable=False)
    tpm = db.Column(db.String(100), nullable=False)
    tpp = db.Column(db.String(100), nullable=False)

# basic stats by season db


class PlayerBasicSeason(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer)
    season = db.Column(db.Integer)
    mpg = db.Column(db.String(100), nullable=False)
    games_played = db.Column(db.String(100), nullable=False)
    games_started = db.Column(db.String(100), nullable=False)
    ppg = db.Column(db.String(100), nullable=False)
    apg = db.Column(db.String(100), nullable=False)
    rpg = db.Column(db.String(100), nullable=False)
    spg = db.Column(db.String(100), nullable=False)
    bpg = db.Column(db.String(100), nullable=False)
    topg = db.Column(db.String(100), nullable=False)
    pfpg = db.Column(db.String(100), nullable=False)
    fta = db.Column(db.String(100), nullable=False)
    ftm = db.Column(db.String(100), nullable=False)
    ftp = db.Column(db.String(100), nullable=False)
    fga = db.Column(db.String(100), nullable=False)
    fgm = db.Column(db.String(100), nullable=False)
    fgp = db.Column(db.String(100), nullable=False)
    tpa = db.Column(db.String(100), nullable=False)
    tpm = db.Column(db.String(100), nullable=False)
    tpp = db.Column(db.String(100), nullable=False)


###############################################################################
# Player Advanced Stats Models
###############################################################################

# player advanced latest db
class PlayerAdvancedLatestModel(db.Model):
    id = db.Column(db.String(100), primary_key=True)
    TS_pctg = db.Column(db.String(100), nullable=False)
    TPAr = db.Column(db.String(100), nullable=False)
    FTr = db.Column(db.String(100), nullable=False)
    ORB_pctg = db.Column(db.String(100), nullable=False)
    DRB_pctg = db.Column(db.String(100), nullable=False)
    TRB_pctg = db.Column(db.String(100), nullable=False)
    AST_pctg = db.Column(db.String(100), nullable=False)
    STL_pctg = db.Column(db.String(100), nullable=False)
    BLK_pctg = db.Column(db.String(100), nullable=False)
    TOV_pctg = db.Column(db.String(100), nullable=False)
    USG_pctg = db.Column(db.String(100), nullable=False)
    OWS = db.Column(db.String(100), nullable=False)
    DWS = db.Column(db.String(100), nullable=False)
    WS = db.Column(db.String(100), nullable=False)
    WS_48 = db.Column(db.String(100), nullable=False)
    OBPM = db.Column(db.String(100), nullable=False)
    DBPM = db.Column(db.String(100), nullable=False)
    BPM = db.Column(db.String(100), nullable=False)
    VORP = db.Column(db.String(100), nullable=False)

# player advanced previous db


class PlayerAdvancedPrevModel(db.Model):
    id = db.Column(db.String(100), primary_key=True)
    TS_pctg = db.Column(db.String(100), nullable=False)
    TPAr = db.Column(db.String(100), nullable=False)
    FTr = db.Column(db.String(100), nullable=False)
    ORB_pctg = db.Column(db.String(100), nullable=False)
    DRB_pctg = db.Column(db.String(100), nullable=False)
    TRB_pctg = db.Column(db.String(100), nullable=False)
    AST_pctg = db.Column(db.String(100), nullable=False)
    STL_pctg = db.Column(db.String(100), nullable=False)
    BLK_pctg = db.Column(db.String(100), nullable=False)
    TOV_pctg = db.Column(db.String(100), nullable=False)
    USG_pctg = db.Column(db.String(100), nullable=False)
    OWS = db.Column(db.String(100), nullable=False)
    DWS = db.Column(db.String(100), nullable=False)
    WS = db.Column(db.String(100), nullable=False)
    WS_48 = db.Column(db.String(100), nullable=False)
    OBPM = db.Column(db.String(100), nullable=False)
    DBPM = db.Column(db.String(100), nullable=False)
    BPM = db.Column(db.String(100), nullable=False)
    VORP = db.Column(db.String(100), nullable=False)

# player advanced latest pctls db


class PlayerAdvancedLatestPctlModel(db.Model):
    id = db.Column(db.String(100), primary_key=True)
    TS_pctg = db.Column(db.String(100), nullable=False)
    TPAr = db.Column(db.String(100), nullable=False)
    FTr = db.Column(db.String(100), nullable=False)
    ORB_pctg = db.Column(db.String(100), nullable=False)
    DRB_pctg = db.Column(db.String(100), nullable=False)
    TRB_pctg = db.Column(db.String(100), nullable=False)
    AST_pctg = db.Column(db.String(100), nullable=False)
    STL_pctg = db.Column(db.String(100), nullable=False)
    BLK_pctg = db.Column(db.String(100), nullable=False)
    TOV_pctg = db.Column(db.String(100), nullable=False)
    USG_pctg = db.Column(db.String(100), nullable=False)
    OWS = db.Column(db.String(100), nullable=False)
    DWS = db.Column(db.String(100), nullable=False)
    WS = db.Column(db.String(100), nullable=False)
    WS_48 = db.Column(db.String(100), nullable=False)
    OBPM = db.Column(db.String(100), nullable=False)
    DBPM = db.Column(db.String(100), nullable=False)
    BPM = db.Column(db.String(100), nullable=False)
    VORP = db.Column(db.String(100), nullable=False)


# player advanced previous pctls db
class PlayerAdvancedPrevPctlModel(db.Model):
    id = db.Column(db.String(100), primary_key=True)
    TS_pctg = db.Column(db.String(100), nullable=False)
    TPAr = db.Column(db.String(100), nullable=False)
    FTr = db.Column(db.String(100), nullable=False)
    ORB_pctg = db.Column(db.String(100), nullable=False)
    DRB_pctg = db.Column(db.String(100), nullable=False)
    TRB_pctg = db.Column(db.String(100), nullable=False)
    AST_pctg = db.Column(db.String(100), nullable=False)
    STL_pctg = db.Column(db.String(100), nullable=False)
    BLK_pctg = db.Column(db.String(100), nullable=False)
    TOV_pctg = db.Column(db.String(100), nullable=False)
    USG_pctg = db.Column(db.String(100), nullable=False)
    OWS = db.Column(db.String(100), nullable=False)
    DWS = db.Column(db.String(100), nullable=False)
    WS = db.Column(db.String(100), nullable=False)
    WS_48 = db.Column(db.String(100), nullable=False)
    OBPM = db.Column(db.String(100), nullable=False)
    DBPM = db.Column(db.String(100), nullable=False)
    BPM = db.Column(db.String(100), nullable=False)
    VORP = db.Column(db.String(100), nullable=False)

# player advanced career db


class PlayerAdvancedCareerModel(db.Model):
    id = db.Column(db.String(100), primary_key=True)
    TS_pctg = db.Column(db.String(100), nullable=False)
    TPAr = db.Column(db.String(100), nullable=False)
    FTr = db.Column(db.String(100), nullable=False)
    ORB_pctg = db.Column(db.String(100), nullable=False)
    DRB_pctg = db.Column(db.String(100), nullable=False)
    TRB_pctg = db.Column(db.String(100), nullable=False)
    AST_pctg = db.Column(db.String(100), nullable=False)
    STL_pctg = db.Column(db.String(100), nullable=False)
    BLK_pctg = db.Column(db.String(100), nullable=False)
    TOV_pctg = db.Column(db.String(100), nullable=False)
    USG_pctg = db.Column(db.String(100), nullable=False)
    OWS = db.Column(db.String(100), nullable=False)
    DWS = db.Column(db.String(100), nullable=False)
    WS = db.Column(db.String(100), nullable=False)
    WS_48 = db.Column(db.String(100), nullable=False)
    OBPM = db.Column(db.String(100), nullable=False)
    DBPM = db.Column(db.String(100), nullable=False)
    BPM = db.Column(db.String(100), nullable=False)
    VORP = db.Column(db.String(100), nullable=False)

# advanced stats by season db


class PlayerAdvancedSeason(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer)
    season = db.Column(db.Integer)
    TS_pctg = db.Column(db.String(100), nullable=False)
    TPAr = db.Column(db.String(100), nullable=False)
    FTr = db.Column(db.String(100), nullable=False)
    ORB_pctg = db.Column(db.String(100), nullable=False)
    DRB_pctg = db.Column(db.String(100), nullable=False)
    TRB_pctg = db.Column(db.String(100), nullable=False)
    AST_pctg = db.Column(db.String(100), nullable=False)
    STL_pctg = db.Column(db.String(100), nullable=False)
    BLK_pctg = db.Column(db.String(100), nullable=False)
    TOV_pctg = db.Column(db.String(100), nullable=False)
    USG_pctg = db.Column(db.String(100), nullable=False)
    OWS = db.Column(db.String(100), nullable=False)
    DWS = db.Column(db.String(100), nullable=False)
    WS = db.Column(db.String(100), nullable=False)
    WS_48 = db.Column(db.String(100), nullable=False)
    OBPM = db.Column(db.String(100), nullable=False)
    DBPM = db.Column(db.String(100), nullable=False)
    BPM = db.Column(db.String(100), nullable=False)
    VORP = db.Column(db.String(100), nullable=False)

##############################################################################################
# Team Info Models
##############################################################################################


class TeamInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    tricode = db.Column(db.String(100), nullable=False)
    conference = db.Column(db.String(100), nullable=False)
    division = db.Column(db.String(100), nullable=False)


class TeamStandings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    wins = db.Column(db.Integer, nullable=False)
    losses = db.Column(db.Integer, nullable=False)
    win_pctg = db.Column(db.String(100), nullable=False)
    loss_pctg = db.Column(db.String(100), nullable=False)
    games_back = db.Column(db.String(100), nullable=False)
    conf_rank = db.Column(db.String(100), nullable=False)
    home_wins = db.Column(db.String(100), nullable=False)
    home_losses = db.Column(db.String(100), nullable=False)
    away_wins = db.Column(db.String(100), nullable=False)
    away_losses = db.Column(db.String(100), nullable=False)
    last_ten_wins = db.Column(db.String(100), nullable=False)
    last_ten_losses = db.Column(db.String(100), nullable=False)
    streak = db.Column(db.String(100), nullable=False)

##############################################################################################
# Team Stats Models
##############################################################################################


class TeamBasicLatestStats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mpg = db.Column(db.String(100), nullable=False)
    fgp = db.Column(db.String(100), nullable=False)
    tpp = db.Column(db.String(100), nullable=False)
    ftp = db.Column(db.String(100), nullable=False)
    orpg = db.Column(db.String(100), nullable=False)
    drpg = db.Column(db.String(100), nullable=False)
    trpg = db.Column(db.String(100), nullable=False)
    apg = db.Column(db.String(100), nullable=False)
    spg = db.Column(db.String(100), nullable=False)
    bpg = db.Column(db.String(100), nullable=False)
    pfpg = db.Column(db.String(100), nullable=False)
    ppg = db.Column(db.String(100), nullable=False)
    oopg = db.Column(db.String(100), nullable=False)
    netppg = db.Column(db.String(100), nullable=False)


class TeamBasicLatestStatsRankings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mpg = db.Column(db.String(100), nullable=False)
    fgp = db.Column(db.String(100), nullable=False)
    tpp = db.Column(db.String(100), nullable=False)
    ftp = db.Column(db.String(100), nullable=False)
    orpg = db.Column(db.String(100), nullable=False)
    drpg = db.Column(db.String(100), nullable=False)
    trpg = db.Column(db.String(100), nullable=False)
    apg = db.Column(db.String(100), nullable=False)
    spg = db.Column(db.String(100), nullable=False)
    bpg = db.Column(db.String(100), nullable=False)
    pfpg = db.Column(db.String(100), nullable=False)
    ppg = db.Column(db.String(100), nullable=False)
    oopg = db.Column(db.String(100), nullable=False)
    netppg = db.Column(db.String(100), nullable=False)


class TeamAdvancedLatestStats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ORTG = db.Column(db.String(100), nullable=False)
    DRTG = db.Column(db.String(100), nullable=False)
    NRTG = db.Column(db.String(100), nullable=False)
    Pace = db.Column(db.String(100), nullable=False)
    FTr = db.Column(db.String(100), nullable=False)
    TPAr = db.Column(db.String(100), nullable=False)
    TS_pctg = db.Column(db.String(100), nullable=False)
    eFG_pctg = db.Column(db.String(100), nullable=False)
    TOV_pctg = db.Column(db.String(100), nullable=False)
    ORB_pctg = db.Column(db.String(100), nullable=False)
    FT_per_FGA = db.Column(db.String(100), nullable=False)
    opp_eFG_pctg = db.Column(db.String(100), nullable=False)
    opp_TOV_pctg = db.Column(db.String(100), nullable=False)
    DRB_pctg = db.Column(db.String(100), nullable=False)
    opp_FT_per_FGA = db.Column(db.String(100), nullable=False)


class TeamAdvancedStatsRankings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ORTG = db.Column(db.String(100), nullable=False)
    DRTG = db.Column(db.String(100), nullable=False)
    NRTG = db.Column(db.String(100), nullable=False)
    Pace = db.Column(db.String(100), nullable=False)
    FTr = db.Column(db.String(100), nullable=False)
    TPAr = db.Column(db.String(100), nullable=False)
    TS_pctg = db.Column(db.String(100), nullable=False)
    eFG_pctg = db.Column(db.String(100), nullable=False)
    TOV_pctg = db.Column(db.String(100), nullable=False)
    ORB_pctg = db.Column(db.String(100), nullable=False)
    FT_per_FGA = db.Column(db.String(100), nullable=False)
    opp_eFG_pctg = db.Column(db.String(100), nullable=False)
    opp_TOV_pctg = db.Column(db.String(100), nullable=False)
    DRB_pctg = db.Column(db.String(100), nullable=False)
    opp_FT_per_FGA = db.Column(db.String(100), nullable=False)

    ##############################################################################################
    # Analysis Models
    ##############################################################################################

    # featured players db


class FeaturedPlayers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    featured_scorer_id = db.Column(db.String(100))
    featured_passer_id = db.Column(db.String(100))
    featured_defender_id = db.Column(db.String(100))

# mvp candidate db


class MVPCandidate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    is_mvp_cand = db.Column(db.Integer)

# trending players db


class TrendingPlayer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    is_improving = db.Column(db.Boolean)

# featured trending players db


class FeaturedTrendingPlayers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    featured_offense_improve_id = db.Column(db.Integer)
    featured_defense_improve_id = db.Column(db.Integer)
    featured_offense_decline_id = db.Column(db.Integer)
    featured_defense_decline_id = db.Column(db.Integer)

# future performance db


class FuturePerformance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mpg = db.Column(db.String(100), nullable=False)
    ppg = db.Column(db.String(100), nullable=False)
    apg = db.Column(db.String(100), nullable=False)
    rpg = db.Column(db.String(100), nullable=False)
    TS_pctg = db.Column(db.String(100), nullable=False)
    BPM = db.Column(db.String(100), nullable=False)


# average basic latest stats (top 30 ppg)
class AverageBasicLatestStatsTop30PPG(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mpg = db.Column(db.String(100), nullable=False)
    games_played = db.Column(db.String(100), nullable=False)
    games_started = db.Column(db.String(100), nullable=False)
    ppg = db.Column(db.String(100), nullable=False)
    apg = db.Column(db.String(100), nullable=False)
    rpg = db.Column(db.String(100), nullable=False)
    spg = db.Column(db.String(100), nullable=False)
    bpg = db.Column(db.String(100), nullable=False)
    topg = db.Column(db.String(100), nullable=False)
    pfpg = db.Column(db.String(100), nullable=False)
    fta = db.Column(db.String(100), nullable=False)
    ftm = db.Column(db.String(100), nullable=False)
    ftp = db.Column(db.String(100), nullable=False)
    fga = db.Column(db.String(100), nullable=False)
    fgm = db.Column(db.String(100), nullable=False)
    fgp = db.Column(db.String(100), nullable=False)
    tpa = db.Column(db.String(100), nullable=False)
    tpm = db.Column(db.String(100), nullable=False)
    tpp = db.Column(db.String(100), nullable=False)

# average advanced latest stats (top 30 ppg)


class AverageAdvancedLatestStatsTop30PPG(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    TS_pctg = db.Column(db.String(100), nullable=False)
    TPAr = db.Column(db.String(100), nullable=False)
    FTr = db.Column(db.String(100), nullable=False)
    ORB_pctg = db.Column(db.String(100), nullable=False)
    DRB_pctg = db.Column(db.String(100), nullable=False)
    TRB_pctg = db.Column(db.String(100), nullable=False)
    AST_pctg = db.Column(db.String(100), nullable=False)
    STL_pctg = db.Column(db.String(100), nullable=False)
    BLK_pctg = db.Column(db.String(100), nullable=False)
    TOV_pctg = db.Column(db.String(100), nullable=False)
    USG_pctg = db.Column(db.String(100), nullable=False)
    OWS = db.Column(db.String(100), nullable=False)
    DWS = db.Column(db.String(100), nullable=False)
    WS = db.Column(db.String(100), nullable=False)
    WS_48 = db.Column(db.String(100), nullable=False)
    OBPM = db.Column(db.String(100), nullable=False)
    DBPM = db.Column(db.String(100), nullable=False)
    BPM = db.Column(db.String(100), nullable=False)
    VORP = db.Column(db.String(100), nullable=False)

# predicted dpoy


class PredictedDPOY(db.Model):
    id = db.Column(db.Integer, primary_key=True)

# predicted mip


class PredictedMIP(db.Model):
    id = db.Column(db.Integer, primary_key=True)


# predicted 6moy


class Predicted6MOY(db.Model):
    id = db.Column(db.Integer, primary_key=True)


# predicted roy


class PredictedROY(db.Model):
    id = db.Column(db.Integer, primary_key=True)
