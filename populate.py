from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlite3
import pandas as pd
import math

conn = sqlite3.connect('example.db')
cur = conn.cursor()

search_query = "SELECT * FROM player"
x = cur.execute(search_query)
print(x.fetchone())

# delete_query = "DELETE FROM player"
# cur.execute(delete_query)
# conn.commit()
# cur.close()

# columnsQuery = ("PRAGMA table_info(%s)" % ("player"))
# columnNames = cur.execute(columnsQuery)
# ans = ""
# ans += "("
# for column in columnNames.fetchall():
#     ans += column[1]
#     ans += ","
# ans += ")"
# print(ans)

# df = pd.read_csv(r'regular_season_stats.csv')
# for index, row in df.iterrows():
#     if index == 0:
#         continue
#     name = row[0]
#     team = row[1]
#     position = row[2]
#     age = row[3]
#     games_played = row[4]
#     minutes_per_game = row[5]
#     minutes_percentage = row[6]
#     usage_rate = row[7]
#     turnover_rate = row[8]
#     free_throws_attempted = row[9]
#     free_throw_percentage = row[10]
#     two_pointers_attempted = row[11]
#     two_pointers_percentage = row[12]
#     three_pointers_attempted = row[13]
#     three_pointers_percentage = row[14]
#     effective_shooting_percentage = row[15]
#     true_shooting_percentage = row[16]
#     points_per_game = row[17]
#     rebounds_per_game = row[18]
#     total_rebound_percentage = row[19]
#     assists_per_game = row[20]
#     assist_percentage = row[21]
#     steals_per_game = row[22]
#     blocks_per_game = row[23]
#     turnovers_per_game = row[24]
#     versatility_index = row[25]
#     offensive_rating = row[26]
#     defensive_rating = row[27]
#     cur.execute("""INSERT INTO player (name,team,position,age,games_played,minutes_per_game,minutes_percentage,usage_rate,turnover_rate,free_throws_attempted,free_throw_percentage,two_pointers_attempted,two_pointers_percentage,three_pointers_attempted,three_pointers_percentage,effective_shooting_percentage,true_shooting_percentage,points_per_game,rebounds_per_game,total_rebound_percentage,assists_per_game,assist_percentage,steals_per_game,blocks_per_game,turnovers_per_game,versatility_index,offensive_rating,defensive_rating) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",(name,team,position,age,games_played,minutes_per_game,minutes_percentage,usage_rate,turnover_rate,free_throws_attempted,free_throw_percentage,two_pointers_attempted,two_pointers_percentage,three_pointers_attempted,three_pointers_percentage,effective_shooting_percentage,true_shooting_percentage,points_per_game,rebounds_per_game,total_rebound_percentage,assists_per_game,assist_percentage,steals_per_game,blocks_per_game,turnovers_per_game,versatility_index,offensive_rating,defensive_rating))
#     conn.commit()
# cur.close()