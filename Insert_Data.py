#!/usr/bin/env python
# coding: utf-8

# Using spycopg2 python library to interact with PostgreSQL and pandas for data manipulation.
# Importing sql queries from sql_queries python file

import psycopg2
import pandas as pd
import boto3
import json
from sql_queries import *


# Connect to the football db


# Function to connect to the database 
def connect_database():
        try: 
            client = boto3.client('secretsmanager',region_name='us-east-1')
            response = client.get_secret_value(
                SecretId='dev/postgress',
            )
    
            respDict=json.loads(response['SecretString'])
            # connect to the default database 
            conn=psycopg2.connect(host=respDict["host"],
                                  dbname="football_db",
                                  user=respDict["username"],
                                  password=respDict["password"])    
            cur=conn.cursor()
        except psycopg2.Error as e:
            raise e

        return conn,cur




# Function to execute the insert query 
def insert_data(conn,cur,file,insert_query):
    for i,row in file.iterrows():
        try:
            cur.execute(insert_query,list(row))
            conn.commit()
        except psycopg2.Error as e:
            print("Error:Inserting records into table")
            print(e)
            conn.rollback()




#calling the function to connect to the db
conn,cur=connect_database()




# CSV file is encoded in latin.
# Quoting flag can be used if the data in csv file is quoted 

players_data=pd.read_csv("Data/players.csv",encoding='latin-1')

teams_data=pd.read_csv("Data/teams.csv",encoding='latin-1',quoting=2)

leagues_data=pd.read_csv("Data/leagues.csv",quoting=2)

games_data=pd.read_csv("Data/games.csv",encoding='latin-1')

shots_data=pd.read_csv("Data/shots.csv",encoding='latin-1')

team_stats=pd.read_csv("Data/teamstats.csv",encoding='latin-1')

player_stats_data=pd.read_csv("Data/playerstats.csv",encoding='latin-1')




# Cleaning the data 
# Only selecting the columns that required for loading into table 
games_data_clean=games_data[["gameID","leagueID","season","date","homeTeamID","awayTeamID","homeGoals","awayGoals","homeProbability","drawProbability"]]

team_stats_clean=team_stats[["gameID","teamID","season","date","location","goals","xGoals","shots","shotsOnTarget","deep"]]

player_stats_data_clean=player_stats_data[["gameID","playerID","goals","ownGoals","shots","xGoals","xGoalsChain","assists","keyPasses"]]




# Validating whether data is in data frame
players_data.head()




teams_data.head()




leagues_data.head()




games_data_clean.head()




shots_data.head()




team_stats_clean.head()




player_stats_data.head()




conn.rollback()




#insert data into players table from dataframe 
insert_data(conn,cur,players_data,players_insert_query)




insert_data(conn,cur,teams_data,teams_insert_query)




insert_data(conn,cur,leagues_data,leagues_insert_query)




for i,row in games_data.iterrows():
    try:
        cur.execute(games_insert_query,(row.gameID,row.leagueID,row.season,pd.to_datetime(row["date"],format='%Y-%m-%d %H:%M:%S'),row.homeTeamID,
                row.awayTeamID,row.homeGoals,row.awayGoals,row.homeProbability,row.drawProbability))
        conn.commit()
    except psycopg2.Error as e:
        print(e)
        conn.rollback()



insert_data(conn,cur,shots_data,shots_insert_query)




for i,row in team_stats_clean.iterrows():
    try:
        cur.execute(team_stats_insert_query,((row.gameID,row.teamID,row.season,pd.to_datetime(row["date"],format='%Y-%m-%d %H:%M:%S'),row.location,
                row.goals,row.xGoals,row.shots,row.shotsOnTarget,row.deep)))
        conn.commit()
    except psycopg2.Error as e:
        print(e)
        conn.rollback()



insert_data(conn,cur,player_stats_data_clean,player_stats_insert_query)



#Fetch the top 5 players in terms of goals
cur.execute(top_players);



print('player_id','player_name','total_goals')
for row in cur:
    print(list(row))


#Closing the connection 
conn.close()






