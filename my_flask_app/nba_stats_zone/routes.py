from nba_stats_zone.models import Player
from flask import flash, redirect, url_for
from nba_stats_zone import app

@app.route('/')
def hello():
    return 'Hello World'