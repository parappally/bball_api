from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/josiahparappally/dev/bball_api/example.db'

db = SQLAlchemy(app)

# conn = sqlite3.connect('example.db')
# cur = conn.cursor()

class Player(db.Model):
    """
    Player table
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    team = db.Column(db.String(200))
    position = db.Column(db.String(200))
    age = db.Column(db.Integer)
    games_played = db.Column(db.Integer)
    minutes_per_game = db.Column(db.Float)
    minutes_percentage = db.Column(db.Float)
    usage_rate = db.Column(db.Float)
    turnover_rate = db.Column(db.Float)
    free_throws_attempted = db.Column(db.Integer)
    free_throw_percentage = db.Column(db.Float)
    two_pointers_attempted = db.Column(db.Integer)
    two_pointers_percentage = db.Column(db.Float)
    three_pointers_attempted = db.Column(db.Integer)
    three_pointers_percentage = db.Column(db.Float)
    effective_shooting_percentage = db.Column(db.Float)
    true_shooting_percentage = db.Column(db.Float)
    points_per_game = db.Column(db.Float)
    rebounds_per_game = db.Column(db.Float)
    total_rebound_percentage = db.Column(db.Float)
    assists_per_game = db.Column(db.Float)
    assist_percentage = db.Column(db.Float)
    steals_per_game = db.Column(db.Float)
    blocks_per_game = db.Column(db.Float)
    turnovers_per_game = db.Column(db.Float)
    versatility_index = db.Column(db.Float)
    offensive_rating = db.Column(db.Float)
    defensive_rating = db.Column(db.Float)

    def __repr__(self):
            return '<Player: {}>'.format(self.name)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/players/<int:player_id>')
def show_player(player_id):    
    search_query = "SELECT * FROM player where id={}".format(player_id)
    conn = sqlite3.connect('example.db')
    result = conn.execute(search_query)
    player_result = result.fetchone()
    if not player_result:
        return "No player with id: {}".format(player_id)
    else:
        ret = {}
        table_columns_query = ("PRAGMA table_info(%s)" % ("player"))
        column_names = conn.execute(table_columns_query)
        index = 0
        for column in column_names.fetchall():
            ret[column[1]] = player_result[index]
            index += 1
        return ret


# conn = sqlite3.connect('example.db')
# cur = conn.cursor()
# cur.execute("""INSERT INTO Player (id,name,team,position,age,games_played,
# minutes_per_game,usage_rate,turnover_rate,free_throws_attempted,
# free_throw_percentage,two_pointers_attempted,two_pointers_percentage,effective_shooting_percentage,true_shooting_percentage,
# points_per_game,rebounds_per_game,total_rebound_percentage,assists_per_game,assists_percentage,
# steals_per_game,blocks_per_game,turnovers_per_game,versatility_index,offensive_rating,defensive_rating) VALUES (?,?,?,?,?,?,?,?,?)""",(nm,addr,city,pin))

