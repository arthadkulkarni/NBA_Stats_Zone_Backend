from nba_stats_zone import db

# set player object, information, and stats
class Player(db.Model):
    __tablename__ = 'player'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    team = db.Column(db.String(10), nullable=False)
    pos = db.Column(db.String(10), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gp = db.Column(db.Integer, nullable=False)
    mpg = db.Column(db.Float, nullable=False)
    usg_per = db.Column(db.Float, nullable=False)
    to_per = db.Column(db.Float)
    fta = db.Column(db.Float)
    ft_per = db.Column(db.Float, nullable=False)
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
        return f"{self.name}" 
    
    # return in json form
    def format_player(self):
        return {
            'id': self.id,
            'name': self.name,
            'team': self.team,
            'pos': self.pos,
            'age': self.age,
            'gp': self.gp,
            'mpg': self.mpg,
            'usg_per': self.usg_per,
            'to_per': self.to_per,
            'fta': self.fta,
            'ft_per': self.ft_per,
            'two_pa': self.two_pa,
            'twop_percent': self.twop_percent,
            'three_pa': self.three_pa,
            'threep_percent': self.threep_percent,
            'efg_percent': self.efg_percent,
            'ts_percent': self.ts_percent,
            'ppg': self.ppg,
            'rpg': self.rpg,
            'apg': self.apg,
            'spg': self.spg,
            'bpg': self.bpg,
            'tpg': self.tpg,
            'points_rebounds': self.points_rebounds,
            'points_assists': self.points_assists,
            'points_assists_rebounds': self.points_assists_rebounds,
            'vi': self.vi,
            'ortg': self.ortg,
            'drtg': self.drtg,
            'year': self.year
        }
    
    def format_rep_player(self):
        return{
            'id': self.id,
            'name': self.name,
            'team': self.team,
            'age': self.age
        }

#set team object, information, and stats
class Team(db.Model):
    __tablename__ = 'team'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    team = db.Column(db.String(20), nullable=False)
    conf = db.Column(db.String(5), nullable=False)
    division = db.Column(db.String(20), nullable=False)
    gp = db.Column(db.Float, nullable=False)
    ppg = db.Column(db.Float, nullable=False)
    oppg = db.Column(db.Float, nullable=False)
    pdiff = db.Column(db.Float, nullable=False)
    pace = db.Column(db.Float, nullable=False)
    oeff = db.Column(db.Float, nullable=False)
    deff = db.Column(db.Float, nullable=False)
    ediff = db.Column(db.Float, nullable=False)
    sos = db.Column(db.Float, nullable=False)
    rsos = db.Column(db.Float, nullable=False)
    sar = db.Column(db.Float, nullable=False)
    cons = db.Column(db.Float, nullable=False)
    a4f = db.Column(db.Float, nullable=False)
    w = db.Column(db.Integer, nullable=False)
    l = db.Column(db.Integer, nullable=False)
    win_percent = db.Column(db.Float, nullable=False)
    ewin_percent = db.Column(db.Float, nullable=False)
    pwin_percent = db.Column(db.Float, nullable=False)
    ach = db.Column(db.Float, nullable=False)
    strk = db.Column(db.Integer, nullable=False)
    year = db.Column(db.String(6), nullable=False)

    def __repr__(self):
        return f"{self.team}({self.year})"
    
    # return in json form
    def format_team(self):
        return{
            'id': self.id,
            'team': self.team,
            'conf': self.conf,
            'division': self.division,
            'gp': self.gp,
            'ppg': self.ppg,
            'oppg': self.oppg,
            'pdiff': self.pdiff,
            'pace': self.pace,
            'oeff': self.oeff,
            'deff': self.deff,
            'ediff': self.ediff,
            'sos': self.sos,
            'rsos': self.rsos,
            'sar': self.sar,
            'cons': self.cons,
            'a4f': self.a4f,
            'w': self.w,
            'l': self.l,
            'win_percent': self.win_percent,
            'ewin_percent': self.ewin_percent,
            'pwin_percent': self.pwin_percent,
            'ach': self.ach,
            'streak': self.strk,
            'year': self.year
        }
    
    def format_rep_team(self):
        return{
            'id': self.id,
            'team': self.team,
            'year': self.year,
            'conference': self.conf
        }
