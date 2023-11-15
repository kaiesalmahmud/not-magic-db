from api_utils import *
from dict_values import *
import json

def listDatabases():
    # result = returnDatabases()
    result = Databases
    result = json.dumps(result)
    return result

def listTables():
    # result = returnTables()
    result = Tables
    result = json.dumps(result)
    return result

def getTableDetails():
    # result = returnTableDetails()
    result = TableDetails
    result = json.dumps(result)
    return result

def getTableRowSamples():
    # result = returnSampleRows()
    result = TableRowSamples
    result = json.dumps(result)
    return result

def getDatabaseExampleResponses():
    # result = returnDatabaseExampleResponse()
    result = DatabaseExampleResponses
    result = json.dumps(result)
    return result

def getDatabaseSpecialInstructions():
    # result = returnDatabaseSpecialInstruction()
    result = DatabaseSpecialInstructions
    result = json.dumps(result)
    return result