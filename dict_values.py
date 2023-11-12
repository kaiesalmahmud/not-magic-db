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

table_dtails = {
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

