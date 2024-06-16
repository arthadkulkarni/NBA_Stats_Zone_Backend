from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@Texas@2014@localhost/Player_Stats'
db = SQLAlchemy(app)

from nba_stats_zone import routes