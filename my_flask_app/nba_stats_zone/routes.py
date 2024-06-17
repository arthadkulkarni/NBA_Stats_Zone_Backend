from nba_stats_zone.models import Player, Team
from flask import redirect, url_for
from nba_stats_zone import app

@app.route('/')
def Welcome():
    return 'Welcome to NBA Stats Zone!'

@app.route('/teams/<year>')
def get_teams(year):
    teams = Team.query.filter_by(year=year)
    teams_list = [team.format_rep_team() for team in teams]
    return {'teams': teams_list}

