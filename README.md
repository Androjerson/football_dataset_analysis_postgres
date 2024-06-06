# 𝐅𝐨𝐨𝐭𝐛𝐚𝐥𝐥 𝐝𝐚𝐭𝐚𝐬𝐞𝐭 𝐚𝐧𝐚𝐥𝐲𝐬𝐢𝐬 𝐰𝐢𝐭𝐡 𝐩𝐨𝐬𝐭𝐠𝐫𝐞𝐬 𝐚𝐧𝐝 𝐩𝐲𝐭𝐡𝐨𝐧 𝐩𝐚𝐧𝐝𝐚𝐬  

![Project Architecture](https://github.com/Androjerson/football_dataset_analysis_postgres/blob/main/Assets/Project%20Architecture.gif)

## Project Description:
This project involves working with comprehensive football dataset covering the Top 5 leagues in Europe from 2014-2020. The analytics team aims to perform some major analysis such as the top players who have scored the most goals.
 
As as a data engineer, my role involved:
1)𝐃𝐚𝐭𝐚 𝐄𝐱𝐭𝐫𝐚𝐜𝐭𝐢𝐨𝐧 :Sourcing the data in 𝘊𝘚𝘝 format
2)𝐃𝐚𝐭𝐚 𝐦𝐚𝐧𝐢𝐩𝐮𝐥𝐚𝐭𝐢𝐨𝐧 𝐚𝐧𝐝 𝐂𝐥𝐞𝐚𝐧𝐢𝐧𝐠:Using 𝘱𝘢𝘯𝘥𝘢𝘴 library in python
3)𝐃𝐚𝐭𝐚 𝐌𝐨𝐝𝐞𝐥𝐥𝐢𝐧𝐠:Building data models based on the source and developing SQL queries
4)𝐃𝐚𝐭𝐚 𝐋𝐨𝐚𝐝𝐢𝐧𝐠:Loading the cleaned and modelled data into 𝘗𝘰𝘴𝘵𝘨𝘳𝘦𝘚𝘘𝘓 using 𝘱𝘴𝘺𝘤𝘰𝘱𝘨2 adapter

This project involves loading CSV files into a relational database for analysis which leverages the strengths of database systems in 𝐝𝐚𝐭𝐚 𝐢𝐧𝐭𝐞𝐠𝐫𝐢𝐭𝐲, 𝐩𝐞𝐫𝐟𝐨𝐫𝐦𝐚𝐧𝐜𝐞 𝐚𝐧𝐝 𝐚𝐝𝐯𝐚𝐧𝐜𝐞𝐝 𝐪𝐮𝐞𝐫𝐲𝐢𝐧𝐠 . This approach gives us upperhand in analysing data over direct CSV analysis ,making it a superior choice for managing and analyzing large and complex datasets

## Tools/Programming Languages used:

1. Python
2. PostgreSQL
3. psycopg2 python PoastgreSQL connector
4. pandas python library
5. AWS secrets manager
6. Boto3 AWS python SDK 

## Dataset:

1. Players
2. Teams
3. Games
4. Shots
5. Leagues
6. TeamStats
7. PlayerStats

## Schema:
![Schema Design](https://github.com/Androjerson/football_dataset_analysis_postgres/blob/main/Assets/schema_design.png)

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
