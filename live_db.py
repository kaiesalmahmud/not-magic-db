import openai
from datetime import date, timedelta
import json
import psycopg2

from dict_values import adiq_db_creds

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


def get_table_info():

    info = table_info

    table_name = info['table_name']
    brief_description = info['brief_description']

    return table_name, brief_description


start_date, end_date = get_daterange()
table_name, brief_description = get_table_info()

message_history = [{"role": "user", 
                    "content": f"""You are a SQL query generator bot for postgreSQL database. 
                    That means you will generate SQL queries for the postgreSQL database.

                    You will generate query for the following table: "{table_name}".
                    {brief_description}

                    The table has the following columns:

                    zone_name: A string field that corresponds to the name of the zone.
                    area_name: A string field that corresponds to the name of the area.
                    point_code: A string field that corresponds to the unique code representing the retail point or store.
                    point_name: A string field that corresponds to the name of the retail point or store.
                    bundle_number: A string field that represents the uniqe tv-box present in the retail point or store.
                    Date: A date field representing a day in the range of {start_date} to {end_date} (Yesterday).
                    Started: A timestamp or datetime representing the start time.
                    Ended: A timestamp or datetime representing the end time.
                    total_play_time_seconds: A numeric field representing the total play time in seconds.
                    total_playtime_minutes: A numeric field representing the total play time in minutes.
                    Total Play Duration: A string representation of the total play time, formatted as HH24:MI:SS.
                    Efficiency: A numeric field representing the efficiency (calculated as the ratio of total play time to expected play time).
                    total_offline_time_seconds: A numeric field representing the total offline time (device disconnected from internet) in seconds.
                    Offline Play Duration: A string representation of the total offline time (device disconnected from internet), formatted as HH24:MI:SS.
                    off_time_seconds: A numeric field representing the off time (device power off due to power cut or load shedding) in seconds.
                    Box Off Duration: A string representation of the off time (device power off due to power cut or load shedding), formatted as HH24:MI:SS.
                    Opened: A string field that indicates whether the box was opened or not (values: 'OPENED' or 'NOT-OPENED').

                    
                    Some sample rows of the table:

                    | zone_name | area_name | point_code | point_name | bundle_number | Date | Started | Ended | total_play_time_seconds | total_playtime_minutes | Total Play Duration | Efficiency | total_offline_time_seconds | Offline Play Duration | off_time_seconds | Box Off Duration | Opened |
                    |-----------|-----------|------------|------------|---------------|------|---------|-------|-------------------------|------------------------|---------------------|------------|----------------------------|-----------------------|------------------|------------------|--------|
                    | T | OFFICE | OFT-001 | AD-IQ HQ | 400 | 2023-10-15 | 2023-10-15 12:00:09.986000+06:00 | 2023-10-15 23:59:51.989000+06:00 | 43190.014000 | 720 | 11:59:50 | 1.1997226111111111 | 0.014000 | 00:00:00 | 0 | 00:00:00 | OPENED |
                    | B | Mohanagor | MNG-001 | Hasib store | 401 | 2023-10-15 | 2023-10-15 09:22:59.988000+06:00 | 2023-10-15 22:04:46.986000+06:00 | 45784.018000 | 763 | 12:43:04 | 1.2717782777777778 | 127.018000 | 00:02:07 | 0 | 00:00:00 | OPENED |
                    | B | Mohanagor | MNG-002 | Seven Eleven | 402 | 2023-10-15 | 2023-10-15 09:01:28.989000+06:00 | 2023-10-15 22:04:13.989000+06:00 | 47055.000000 | 784 | 13:04:15 | 1.3070833333333333 | 0 | 00:00:00 | 0 | 00:00:00 | OPENED |
                    | B | Mohanagor | MNG-003 | Shasroyie Super Shop | 403 | 2023-10-15 | 2023-10-15 09:01:38.992000+06:00 | 2023-10-15 22:04:25.986000+06:00 | 47056.994000 | 784 | 13:04:16 | 1.3071387222222222 | 0 | 00:00:00 | 0 | 00:00:00 | OPENED |
                    | B | Mohanagor | MNG-004 | Chistia Depertmental Store | 404 | 2023-10-15 | 2023-10-15 09:23:00.991000+06:00 | 2023-10-15 22:04:45.986000+06:00 | 45794.995000 | 763 | 12:43:14 | 1.2720831944444444 | 0 | 00:00:00 | 0 | 00:00:00 | OPENED |

                    Some sample natural language questions and their corresponding SQL queries:

                    1.
                    Question:
                    What are the names of the zones? 
                    Query:
                    SELECT DISTINCT "zone_name"
                    FROM "dailyLog"
                    ORDER BY "zone_name"

                    2.
                    Question:
                    What is the number of retail points and total play time in minutes for each zone? 
                    Query:
                    SELECT "zone_name", COUNT(DISTINCT "point_code"), SUM(total_playtime_minutes)
                    FROM "dailyLog"
                    GROUP BY "zone_name"

                    3.
                    Question:
                    How many shops achieved satisfactory efficiency on 15th October?
                    Query:
                    SELECT "zone_name", COUNT(DISTINCT "point_code"), SUM(total_playtime_minutes) 
                    FROM "dailyLog" 
                    WHERE "Efficiency" >= 1 AND "Date" = '2023-10-15'
                    GROUP BY "zone_name"

                    4.
                    Question:
                    How many shops were not opened on 15th October?
                    Query:
                    SELECT "zone_name", COUNT(DISTINCT "point_code")
                    FROM "dailyLog" 
                    WHERE "Opened" = 'NOT-OPENED' AND "Date" = '2023-10-15'
                    GROUP BY "zone_name"

                    5.
                    Question:
                    List of names of the shops that were not opened on 15th October?
                    Query:
                    SELECT "zone_name", "point_code", "point_name"
                    FROM "dailyLog" 
                    WHERE "Opened" = 'NOT-OPENED' AND "Date" = '2023-10-15'

                    6.
                    Question:
                    What is the number and total playtime for under-performing shops on 15th October?
                    Query:
                    SELECT "zone_name", COUNT(DISTINCT "point_code"), SUM(total_playtime_minutes) 
                    FROM "dailyLog" 
                    WHERE "Opened" = 'OPENED' AND "Efficiency" < 1 AND "Date" = '2023-10-15'
                    GROUP BY "zone_name"

                    7.
                    Question:
                    How many shops opend after 10 AM but before 11 AM on 15th October?
                    Query:
                    SELECT "zone_name", COUNT(DISTINCT "point_code") 
                    FROM "dailyLog" 
                    WHERE EXTRACT(HOUR FROM "Started") >= 10 AND EXTRACT(HOUR FROM "Started") < 11 AND "Date" = '2023-10-15'
                    GROUP BY "zone_name"

                    8.
                    Question:
                    Which shop had the highest efficiency on 15th October?
                    Query:
                    SELECT "point_name", MAX("Efficiency")
                    FROM "dailyLog"
                    WHERE "Date" = '2023-10-15' AND "Efficiency" IS NOT NULL
                    GROUP BY "point_name"
                    ORDER BY MAX("Efficiency") DESC

                    ---------------------------------------------

                    I will ask a question about the data in natural language in my message, and you will reply only with a SQL query 
                    that will generate the necessary response when performed on the postgreSQL database. 
                    Reply only with the sql query to further input. If you understand, say OK."""},
                   {"role": "assistant", 
                    "content": f"OK"}]