from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/josiahparappally/dev/bball_api/example.db'

db = SQLAlchemy(app)

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

@app.route('/players/stat/<statistic_id>')
def show_ordered_statistics(statistic_id):
    conn = sqlite3.connect('example.db')
    table_columns_query = ("PRAGMA table_info(%s)" % ("player"))
    query_result = conn.execute(table_columns_query)
    column_names = query_result.fetchall()
    statistic_index = -1
    for index in range(len(column_names)):
        if column_names[index][1] == statistic_id:
            statistic_index = index
    if statistic_index == -1:
        return "No statistic called: {}".format(statistic_id)
    else:
        lst = []
        search_query = "SELECT * FROM player"
        query_result = conn.execute(search_query)
        players = query_result.fetchall()
        for player in players:
            if player[statistic_index]:
                lst.append([player[1], player[statistic_index]])
        lst.sort(reverse=True, key=lambda player: player[1])
        return jsonify(lst)

