from nba_stats_zone import db

# set player object, information, and stats
class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    team = db.Column(db.String(10), nullable=False)
    position = db.Column(db.String(10), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    games_played = db.Column(db.Integer, nullable=False)
    minutes_per_game = db.Column(db.Float, nullable=False)
    usg_percent = db.Column(db.Float, nullable=False)
    to_percent = db.Column(db.Float)
    fta = db.Column(db.Float)
    ft_percent = db.Column(db.Float, nullable=False)
    two_pa = db.Column(db.Float, nullable=False)
    twop_percent = db.Column(db.Float, nullable=False)
    three_pa = db.Column(db.Float, nullable=False)
    threep_percent = db.Column(db.Float, nullable=False)
    efg_percent = db.Column(db.Float)
    ts_percent = db.Column(db.Float)
    ppg = db.Column(db.Float, nullable=False)
    rpg = db.Column(db.Float, nullable=False)
    apg = db.Column(db.Float, nullable=False)
    spg = db.Column(db.Float, nullable=False)
    bpg = db.Column(db.Float, nullable=False)
    tpg = db.Column(db.Float, nullable=False)
    points_rebounds = db.Column(db.Float, nullable=False)
    points_assists = db.Column(db.Float, nullable=False)
    points_assists_rebounds = db.Column(db.Float, nullable=False)
    vi = db.Column(db.Float, nullable=False)
    ortg = db.Column(db.Float)
    drtg = db.Column(db.Float)
    year = db.Column(db.String(7), nullable=False)

    def __repr__(self):
        return "{self.name}"