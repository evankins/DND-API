import os
from .db_utils import *

def rebuild_tables():
    exec_sql_file('src/db/schema.sql')
    exec_sql_file('src/db/test_data.sql')

def list_users():
    """DB layer call for listing all attendees."""
    return exec_get_all('SELECT * FROM characters')