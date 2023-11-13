adiq_db_pass = open('adiq_db_pass.txt', 'r').read().strip()

adiq_db_creds = {
    "host" : "server-alpha.ad-iq.com",
    "port" : "32974",
    "db" : "adiq",
    "username" : "mlteam",
    "password" : adiq_db_pass
}


#############################

Databases = {
    "input": "",
    "databases": [
        {
            "name": "adiq", 
            "description": "This database contains information about the daily log of retail points or shops in a particular area. A number of areas form a zone."
        }
    ]
}

Tables = {
    "input": {
        "database_name" : "adiq"
    },
    "tables": [
        {
            "name": "dailyLog",
            "description": "This table contains information about the daily log of retail points or shops in a particular area. A number of areas form a zone."
        }
    ]
}

TableDetails = {
    "input": {
        "database_name": "adiq",
        "table_name": "dailyLog"
    },
    "columns": [
        {
            "name": "zone_name",
            "description": "A string field that corresponds to the name of the zone."
        },
        {
            "name": "area_name",
            "description": "A string field that corresponds to the name of the area."
        },
        {
            "name": "point_code",
            "description": "A string field that corresponds to the unique code representing the retail point or store."
        },
        {
            "name": "point_name",
            "description": "A string field that corresponds to the name of the retail point or store."
        },
        {
            "name": "bundle_number",
            "description": "A string field that represents the uniqe tv-box present in the retail point or store."
        },
        {
            "name": "Date",
            "description": "A date field representing the day of the record."
        },
        {
            "name": "Started",
            "description": "A timestamp or datetime representing the start time."
        },
        {
            "name": "Ended",
            "description": "A timestamp or datetime representing the end time."
        },
        {
            "name": "total_play_time_seconds",
            "description": "A numeric field representing the total play time in seconds."
        },
        {
            "name": "total_playtime_minutes",
            "description": "A numeric field representing the total play time in minutes."
        },
        {
            "name": "Total Play Duration",
            "description": "A string representation of the total play time, formatted as HH24:MI:SS."
        },
        {
            "name": "Efficiency",
            "description": "A numeric field representing the efficiency (calculated as the ratio of total play time to expected play time)."
        },
        {
            "name": "total_offline_time_seconds",
            "description": "A numeric field representing the total offline time (device disconnected from internet) in seconds."
        },
        {
            "name": "Offline Play Duration",
            "description": "A string representation of the total offline time (device disconnected from internet), formatted as HH24:MI:SS."
        },
        {
            "name": "off_time_seconds",
            "description": "A numeric field representing the off time (device power off due to power cut or load shedding) in seconds."
        },
        {
            "name": "Box Off Duration",
            "description": "A string representation of the off time (device power off due to power cut or load shedding), formatted as HH24:MI:SS."
        },
        {
            "name": "Opened",
            "description": "A string field that indicates whether the box was opened or not (values: 'OPENED' or 'NOT-OPENED')."
        }
    ]
}

TableRowSampes = {
    "input": {
        "database_name": "adiq",
        "table_name": "dailyLog"
    },
    "sample_rows": [
        "| T | OFFICE | OFT-001 | AD-IQ HQ | 400 | 2023-10-15 | 2023-10-15 12:00:09.986000+06:00 | 2023-10-15 23:59:51.989000+06:00 | 43190.014000 | 720 | 11:59:50 | 1.1997226111111111 | 0.014000 | 00:00:00 | 0 | 00:00:00 | OPENED |",
        "| B | Mohanagor | MNG-001 | Hasib store | 401 | 2023-10-15 | 2023-10-15 09:22:59.988000+06:00 | 2023-10-15 22:04:46.986000+06:00 | 45784.018000 | 763 | 12:43:04 | 1.2717782777777778 | 127.018000 | 00:02:07 | 0 | 00:00:00 | OPENED |",
        "| B | Mohanagor | MNG-002 | Seven Eleven | 402 | 2023-10-15 | 2023-10-15 09:01:28.989000+06:00 | 2023-10-15 22:04:13.989000+06:00 | 47055.000000 | 784 | 13:04:15 | 1.3070833333333333 | 0 | 00:00:00 | 0 | 00:00:00 | OPENED |",
        "| B | Mohanagor | MNG-003 | Shasroyie Super Shop | 403 | 2023-10-15 | 2023-10-15 09:01:38.992000+06:00 | 2023-10-15 22:04:25.986000+06:00 | 47056.994000 | 784 | 13:04:16 | 1.3071387222222222 | 0 | 00:00:00 | 0 | 00:00:00 | OPENED |",
        "| B | Mohanagor | MNG-004 | Chistia Depertmental Store | 404 | 2023-10-15 | 2023-10-15 09:23:00.991000+06:00 | 2023-10-15 22:04:45.986000+06:00 | 45794.995000 | 763 | 12:43:14 | 1.2720831944444444 | 0 | 00:00:00 | 0 | 00:00:00 | OPENED |"
    ]
}

DatabaseExampleResponses = {
    "input": {
        "database_name": "adiq"
    },
    "examples": [
        {
            "query": "What are the names of the zones?",
            "response": "SELECT DISTINCT \"zone_name\"\nFROM \"dailyLog\"\nORDER BY \"zone_name\""
        },
        {
            "query": "What is the number of retail points and total play time in minutes for each zone?",
            "response": "SELECT \"zone_name\", COUNT(DISTINCT \"point_code\"), SUM(total_playtime_minutes)\nFROM \"dailyLog\"\nGROUP BY \"zone_name\""
        },
        {
            "query": "How many shops achieved satisfactory efficiency on 15th October?",
            "response": "SELECT \"zone_name\", COUNT(DISTINCT \"point_code\"), SUM(total_playtime_minutes) \nFROM \"dailyLog\" \nWHERE \"Efficiency\" >= 1 AND \"Date\" = '2023-10-15'\nGROUP BY \"zone_name\""
        },
        {
            "query": "How many shops were not opened on 15th October?",
            "response": "SELECT \"zone_name\", COUNT(DISTINCT \"point_code\")\nFROM \"dailyLog\" \nWHERE \"Opened\" = 'NOT-OPENED' AND \"Date\" = '2023-10-15'\nGROUP BY \"zone_name\""
        },
        {
            "query": "List of names of the shops that were not opened on 15th October?",
            "response": "SELECT \"zone_name\", \"point_code\", \"point_name\"\nFROM \"dailyLog\" \nWHERE \"Opened\" = 'NOT-OPENED' AND \"Date\" = '2023-10-15'"
        },
        {
            "query": "What is the number and total playtime for under-performing shops on 15th October?",
            "response": "SELECT \"zone_name\", COUNT(DISTINCT \"point_code\"), SUM(total_playtime_minutes) \nFROM \"dailyLog\" \nWHERE \"Efficiency\" < 1 AND \"Date\" = '2023-10-15'\nGROUP BY \"zone_name\""
        }
    ]
}

DatabaseSpecialInstructions = {
    "input": {
        "database_name": "adiq"
    },
    "instructions": [
        ""
    ]
}