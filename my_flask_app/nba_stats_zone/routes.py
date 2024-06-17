from nba_stats_zone.models import Player, Team
from nba_stats_zone import app

@app.route('/')
def Welcome():
    return 'Welcome to NBA Stats Zone!'

#route returns the names and years of each team
@app.route('/teams/<year>')
def get_teams(year):
    teams = Team.query.filter_by(year=year).all()
    teams_list = [team.format_rep_team() for team in teams]
    return {'teams': teams_list}

# route returns the advanced stats for a certain team
@app.route('/teams/<year>/<int:id>')
def display_team_stats(year, id):
    team = Team.query.filter_by(year=year, id=id).first_or_404()
    return {'team': team.format_team()}

#route returns the names and basic information of each player
@app.route('/players/<year>')
def get_players(year):
    players = Player.query.filter_by(year=year).all()
    player_list = [player.format_rep_player() for player in players]
    return {'players': player_list}
