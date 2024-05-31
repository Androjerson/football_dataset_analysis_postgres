#CREATE queries

players_create_table=("""CREATE TABLE IF NOT EXISTS players(id INT PRIMARY KEY,name VARCHAR NOT NULL);""")

teams_create_table=("""CREATE TABLE IF NOT EXISTS teams(id INT PRIMARY KEY,name VARCHAR NOT NULL);""")

leagues_create_table=("""CREATE TABLE IF NOT EXISTS leagues(id INT PRIMARY KEY,name VARCHAR NOT NULL,u_notation VARCHAR);""")

games_create_table=("""CREATE TABLE IF NOT EXISTS games(id INT PRIMARY KEY , league_id INT REFERENCES leagues, season INT , date TIMESTAMP , 
                    homeTeam_id INT REFERENCES teams, awayTeam_id INT REFERENCES teams , home_goals INT , away_goals INT , home_prob NUMERIC, draw_probability                       NUMERIC);""")

shots_create_table=("""CREATE TABLE IF NOT EXISTS shots(game_id INT REFERENCES games, shooter_id INT REFERENCES players, assister_id NUMERIC, minute INT ,                           situation VARCHAR , lastAction VARCHAR , shotType VARCHAR , shotResult VARCHAR , xpct_goals NUMERIC, positionX NUMERIC,positionY                                 NUMERIC);""")

team_stats_create_table=("""CREATE TABLE IF NOT EXISTS team_stats(game_id INT REFERENCES games , team_id INT REFERENCES teams , season INT , date TIMESTAMP ,
                         loc_indc VARCHAR , goals INT , xpct_goals NUMERIC , shots INT , shotsOnTarget INT , deep INT);""")

player_stats_create_table=("""CREATE TABLE IF NOT EXISTS player_stats(game_id INT REFERENCES games, player_id INT REFERENCES players , goals INT , own_goal INT,
                           shots INT , xpct_goals NUMERIC , xpct_goals_chains NUMERIC , assists INT , keypass INT);""")

#INSERT queries
players_insert_query=("""INSERT INTO players(id,name)VALUES(%s,%s);""")
teams_insert_query=("""INSERT INTO teams(id,name) VALUES(%s,%s);""")
leagues_insert_query=("""INSERT INTO leagues(id,name,u_notation) VALUES(%s,%s,%s);""")
games_insert_query=("""INSERT INTO games(id,league_id,season,date,homeTeam_id,awayTeam_id,home_goals,away_goals,home_prob,draw_probability) \
                    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);""")
shots_insert_query=("""INSERT INTO shots(game_id,shooter_id,assister_id,minute,situation,lastAction,shotType,shotResult,xpct_goals,positionX,positionY)\
                    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);""")
team_stats_insert_query=("""INSERT INTO team_stats(game_id,team_id,season,date,loc_indc,goals,xpct_goals,shots,shotsOnTarget,deep)\
                         VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);""")
player_stats_insert_query=("""INSERT INTO player_stats(game_id,player_id,goals,own_goal,shots,xpct_goals,xpct_goals_chains,assists,keypass)\
                           VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);""")

#TEST queries
players_select=("""SELECT * FROM players LIMIT 5;""")
teams_select=("""SELECT * FROM teams LIMIT 5;""")
leagues_select=("""SELECT * FROM leagues LIMIT 5;""")
games_select=("""SELECT * FROM games LIMIT 5;""")
shots_select=("""SELECT * FROM shots LIMIT 5;""")
team_stats_select=("""SELECT * FROM team_stats LIMIT 5;""")
players_stats_select=("""SELECT * FROM players LIMIT 5;""")



#SELECT queries
top_players= ("""SELECT ps.player_id,p.name,SUM(ps.goals) AS total_goals FROM player_stats ps JOIN players p ON ps.player_id=p.id GROUP
BY ps.player_id,p.name ORDER BY total_goals DESC LIMIT 5;""")


# create queries in list
create_table_queries = [players_create_table, teams_create_table, leagues_create_table, games_create_table, shots_create_table,team_stats_create_table,player_stats_create_table]
