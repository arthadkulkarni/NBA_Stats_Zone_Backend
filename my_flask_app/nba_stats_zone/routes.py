from nba_stats_zone.models import Player, Team
from nba_stats_zone import app

@app.route('/')
def Welcome():
    return 'Welcome to NBA Stats Zone!'

#route returns the names and years of each team
@app.route('/team-stats')
def get_teams():
    teams = Team.query.filter_by().all()
    teams_list = [team.format_rep_team() for team in teams]
    return {'players': teams_list}


# route returns the advanced stats for a certain team
@app.route('/team-stats/<year>/<int:id>')
def display_team_stats(year, id):
    team = Team.query.filter_by(year=year, id=id).first_or_404()
    return {'team': team.format_team()}

# route returns the names and basic information of each player
@app.route('/player-stats')
def get_players():
    players = Player.query.filter_by().all()
    player_list = [player.format_rep_player() for player in players]
    return {'players': player_list}

# route returns the advanced stats for a certain player
@app.route('/player-stats/<year>/<int:id>')
def display_player_stats(year, id):
    player = Player.query.filter_by(year=year, id=id).first_or_404()
    return {'player': player.format_player()}
