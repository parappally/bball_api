from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/josiahparappally/dev/bball_api/example.db'

db = SQLAlchemy(app)

minutes_flag = False
minutes_amount = 15

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

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/players', methods=['GET'])
def show_all_players():
    conn = sqlite3.connect('example.db')
    search_query = "SELECT * FROM player"
    result = conn.execute(search_query).fetchall()
    d = {}
    for player in result:
        d[player[1]] = player[0]
    return d

@app.route('/players/<int:player_id>', methods=['GET'])
def show_player(player_id):    
    conn = sqlite3.connect('example.db')
    search_query = "SELECT * FROM player where id={}".format(player_id)
    result = conn.execute(search_query).fetchone()
    if not result:
        return "No player with id: {}".format(player_id)
    else:
        ret = {}
        table_columns_query = ("PRAGMA table_info(%s)" % ("player"))
        column_names = conn.execute(table_columns_query)
        index = 0
        for column in column_names.fetchall():
            ret[column[1]] = result[index]
            index += 1
        return ret

@app.route('/players/stat/<string:statistic_id>', methods=['GET'])
def show_ordered_statistics(statistic_id):
    conn = sqlite3.connect('example.db')
    table_columns_query = ("PRAGMA table_info(%s)" % ("player"))
    query_result = conn.execute(table_columns_query).fetchall()
    statistic_index = -1
    for index in range(len(query_result)):
        if query_result[index][1] == statistic_id:
            statistic_index = index
    if statistic_index == -1:
        return "No statistic called: {}".format(statistic_id)
    else:
        lst = []
        if minutes_flag:
            search_query = "SELECT * FROM player where minutes_per_game > {}".format(minutes_amount)
        else:
            search_query = "SELECT * FROM player"
        query_result = conn.execute(search_query).fetchall()
        for player in query_result:
            d = {}
            if player[statistic_index]:
                d["name"] = player[1]
                d[statistic_id] = player[statistic_index]
                lst.append(d)
        lst.sort(reverse=True, key=lambda player: player[statistic_id])
        return jsonify(lst)

