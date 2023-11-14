import openai
from datetime import date, timedelta
import json
import psycopg2

from dict_values import adiq_db_creds
from utils import *

openai.api_key = open('openai_key.txt', 'r').read().strip()

def get_db_connection():

    creds = adiq_db_creds

    conn = psycopg2.connect(
        host=creds['host'],
        port=creds['port'],
        dbname=creds['db'],
        user=creds['username'],
        password=creds['password']
    )
    return conn

def get_daterange():

    yesterday = str(date.today() - timedelta(days=1))
    yesterday = "'"+yesterday+"'"

    start_date = "'2023-07-01'"
    end_date = yesterday

    return start_date, end_date

start_date, end_date = get_daterange()
Databases = listDatabases()
Tables = listTables()
TableDetails = getTableDetails()
TableRowSamples = getTableRowSamples()
DatabaseExampleResponses = getDatabaseExampleResponses()

message_history = [{"role": "user", 
                    "content": f"""You are a SQL query generator bot for postgreSQL database. 
                    That means you will generate SQL queries for a postgreSQL database.

                    Following json contains the list of databases and their brief descriptions:
                    {Databases}

                    The database contains the following tables:
                    {Tables}

                    The following json contains the details of the table:
                    {TableDetails}
                    
                    Some sample rows of the table:
                    {TableRowSamples}

                    Some sample natural language questions and their corresponding SQL queries:
                    {DatabaseExampleResponses}
                    

                    ---------------------------------------------

                    I will ask a question about the data in natural language in my message, and you will reply only with a SQL query 
                    that will generate the necessary response when performed on the postgreSQL database. 
                    Reply only with the sql query to further input. If you understand, say OK."""},
                   {"role": "assistant", 
                    "content": f"OK"}]