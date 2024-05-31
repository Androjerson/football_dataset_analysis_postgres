#!/usr/bin/env python
# coding: utf-8

# Using spycopg2 python library to interact with PostgreSQL and pandas for data manipulation


import psycopg2
import pandas as pd
import boto3
import json
from sql_queries import create_table_queries


# Creating a user-defined function to connect and create PostgreSQL. Also intialize in-built functions to execute SQL queries


def create_database():
        
        """
        -creates and connects to the football DB
        -returns the connection and cursor to football DB 
        """
        try: 
            client = boto3.client('secretsmanager',region_name='us-east-1')
            response = client.get_secret_value(
                SecretId='dev/postgress',
            )
    
            respDict=json.loads(response['SecretString'])
            # connect to the default database 
            conn=psycopg2.connect(host=respDict["host"],
                                  dbname="postgres",
                                  user=respDict["username"],
                                  password=respDict["password"])
            conn.set_session(autocommit=True)
            cur=conn.cursor()
                
            # create the football db 
            cur.execute("DROP DATABASE football_db")
            cur.execute("CREATE DATABASE football_db")
    
            #closing the connection to the default db 
            conn.close()
        
            # connect to the football db
            conn=psycopg2.connect(host=respDict["host"],
                                  dbname="football_db",
                                  user=respDict["username"],
                                  password=respDict["password"])
            print(respDict["host"],respDict["username"],respDict["password"])
            cur=conn.cursor()
            print(cur)
            conn.set_session(autocommit=True)
        except psycopg2.Error as e:
            print("Error in creating the database")
            raise e

        return conn,cur

#creating a function to create tables 

def create_tables(conn,cur):
    for i in create_table_queries:
        cur.execute(i)
        conn.commit()

# Calling the create database function to get the connection and cursor string

conn,cur=create_database()
create_tables(conn,cur)
conn.close()




