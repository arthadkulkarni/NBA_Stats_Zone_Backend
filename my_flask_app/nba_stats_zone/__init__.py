from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@127.0.0.1/Player_Stats'
db = SQLAlchemy(app)
CORS(app)

from nba_stats_zone import routes