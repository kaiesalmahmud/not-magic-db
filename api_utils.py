import requests
import json 
from urllib.parse import quote

def returnEncodedData(data):
    data = {"json":data}
    
    json_data = json.dumps(data)
    encoded_data = quote(json_data)
    
    return encoded_data

def returnDatabases():
    r = requests.get('http://aristotle.fringecore.sh/rpc/ml/data.getDatabases')
    response = r.json() 
    result = response['result']['data']['json']
    return result

def returnTables():
    r = requests.get("http://aristotle.fringecore.sh/rpc/ml/data.getTables?input="+returnEncodedData(
        {
            "database_name":"adiq"
        }
    ))
    response = r.json() 
    result = response['result']['data']['json']
    return result

def returnTableDetails():
    r = requests.get("http://aristotle.fringecore.sh/rpc/ml/data.getTableDetails?input="+returnEncodedData(
        {
            "database_name":"adiq",
            "table_name": "dailyLog"
        }
    ))
    response = r.json() 
    result = response['result']['data']['json']
    return result

def returnSampleRows():
    r = requests.get("http://aristotle.fringecore.sh/rpc/ml/data.getTableRowSamples?input="+returnEncodedData(
        {
            "database_name":"adiq",
            "table_name": "dailyLog"
        }
    ))
    response = r.json() 
    result = response['result']['data']['json']
    return result

def returnDatabaseExampleResponse():
    r = requests.get("http://aristotle.fringecore.sh/rpc/ml/data.getDatabaseExampleResponse?input="+returnEncodedData(
        {
            "database_name":"adiq"
        }
    ))
    response = r.json() 
    result = response['result']['data']['json']
    return result

def returnDatabaseSpecialInstruction():
    r = requests.get("http://aristotle.fringecore.sh/rpc/ml/data.getDatabaseSpecialInstructions?input="+returnEncodedData(
        {
            "database_name":"adiq"
        }
    ))
    response = r.json() 
    result = response['result']['data']['json']
    return result