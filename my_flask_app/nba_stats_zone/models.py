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
    twopa = db.Column(db.Float, nullable=False)
    twop_per = db.Column(db.Float, nullable=False)
    threepa = db.Column(db.Float, nullable=False)
    threep_per = db.Column(db.Float, nullable=False)
    efg_per = db.Column(db.Float)
    ts_per = db.Column(db.Float)
    ppg = db.Column(db.Float, nullable=False)
    rpg = db.Column(db.Float, nullable=False)
    apg = db.Column(db.Float, nullable=False)
    spg = db.Column(db.Float, nullable=False)
    bpg = db.Column(db.Float, nullable=False)
    tpg = db.Column(db.Float, nullable=False)
    p_r = db.Column(db.Float, nullable=False)
    p_a = db.Column(db.Float, nullable=False)
    p_r_a = db.Column(db.Float, nullable=False)
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
            'two_pa': self.twopa,
            'twop_percent': self.twop_per,
            'three_pa': self.threepa,
            'threep_percent': self.threep_per,
            'efg_percent': self.efg_per,
            'ts_percent': self.ts_per,
            'ppg': self.ppg,
            'rpg': self.rpg,
            'apg': self.apg,
            'spg': self.spg,
            'bpg': self.bpg,
            'tpg': self.tpg,
            'points_rebounds': self.p_r,
            'points_assists': self.p_a,
            'points_assists_rebounds': self.p_r_a,
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
            'age': self.age,
            'year': self.year
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
            'conference': self.conf,
            'division': self.division
        }
