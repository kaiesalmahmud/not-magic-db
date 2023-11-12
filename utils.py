def list_databases():
    response = client.call_api('listDatabases', {})
    return response

def list_tables(database_name):
    response = client.call_api('listTables', {'database_name': database_name})
    return response

def get_table_details(database_name, table_name):
    response = client.call_api('getTableDetails', {
        'database_name': database_name,
        'table_name': table_name
    })
    return response

def get_table_row_samples(database_name, table_name):
    response = client.call_api('getTableRowSampes', {
        'database_name': database_name,
        'table_name': table_name
    })
    return response

def get_database_example_responses(database_name):
    response = client.call_api('getDatabaseExampleResponses', {'database_name': database_name})
    return response

def get_database_special_instructions(database_name):
    response = client.call_api('getDatabaseSpecialInstructions', {'database_name': database_name})
    return response

def get_table_special_instructions(database_name, table_name):
    response = client.call_api('getTableSpecialInstructions', {
        'database_name': database_name,
        'table_name': table_name
    })
    return response

def update_waiting_message(chat_id, updated_message):
    response = client.call_api('updateWaitingMessage', {
        'chat_id': chat_id,
        'updated_message': updated_message
    })
    return response

def update_chat_title(chat_id, updated_title):
    response = client.call_api('updateChatTitle', {
        'chat_id': chat_id,
        'updated_title': updated_title
    })
    return response

def run_sql(database_name, sql):
    response = client.call_api('runSQL', {
        'database_name': database_name,
        'sql': sql
    })
    return response