# Football Dataset: data modelling with postgres and python libraries  

![Project Architecture](https://github.com/Androjerson/football_dataset_analysis_postgres/blob/main/Project%20Architecture.gif)

## Project Description:
Football dataset is  football-related data covering the Top5 leagues in Europe from 2014-2020. The analytics team wants to perform some major analysis such as 
the top players scored the most goals.
We as a data engineer, our role is 
1. To get the data from source which is in CSV format
2. Do data manipulation and data cleaning  with the help of pandas python library
3. Load the data into PostgreSQL with the python postgres connector psycopg2

## Dataset:

1. Players
2. Teams
3. Games
4. Shots
5. Leagues
6. TeamStats
7. PlayerStats

## Schema:
![Schema Design](https://github.com/Androjerson/football_dataset_analysis_postgres/blob/main/schema_design.png)

### Dimension Tables:
* players:Basic players information
    id,name
* teams:Basic teams information
    id,name
* leagues:Basic leagues information with League name in understat notation
    id,name,u_notation
* games:Detailed game information with team ids,goals,goal probability
    id,league_id,season,date,homeTeam_id,awayTeam_id,home_goals,away_goals,home_prob,draw_probability

### Fact Tables:
  * shots:Statistical information of each shot targeting goal played in the game
     game_id,shooter_id,assister_id,minute,situation,lastAction,shotType,shotResult,xpct_goals,positionX,positionY
  * team_stats:Statistical information of each team
      game_id,team_id,season,date,loc_indc,goals,xpct_goals,shots,shotsOnTarget,deep
  * player_stats:Statistical information of each player
      game_id,player_id,goals,own_goal,shots,xpct_goals,xpct_goals_chains,assists,keypass

## Files

Create Table.ipynb: Establishes connection with PostgreSQL and resets all the table in database

Insert_Data.ipynb: Establishes connection with PostgreSQL with the help of psycopg2 and AWS Secrets Manager.Reads data from csv and store it in dataframe via python Pandas.
                  Do some data cleaning and datatype casting.Load it into postgres database. Validate the data presence in table via test queries .Run the analysis query on it

sql_queries.py : Create,Insert,Test and Select queries which is used in the above two files

## Build ETL pipeline:

1. Run the <b>Create Table.ipynb</b> to create the database and tables
2. Run the <b>Insert_Data.ipynb</b> to load the data from csv file to PostgreSQL, run validataions and analysis
