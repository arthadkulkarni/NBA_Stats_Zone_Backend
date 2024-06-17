from nba_stats_zone.models import Player, Team
from flask import redirect, url_for
from nba_stats_zone import app

@app.route('/')
def Welcome():
    return 'Welcome to NBA Stats Zone!'

@app.route('/team/<year>', methods = ['GET'])
def get_teams(year):
    teams = Team.query.order_by(Team.id.asc()).filter_by(year=year)
    teams_list = [Team.format_team() for team in teams]
    return {'teams': teams_list}
