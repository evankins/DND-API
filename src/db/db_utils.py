import psycopg2
import yaml
import os

def connect():
    config = {}
    yml_path = os.path.join(os.path.dirname(__file__), '../../config/db.yml')
    with open(yml_path, 'r') as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
    return psycopg2.connect(dbname=config['database'],
                            user=config['user'],
                            password=config['password'],
                            host=config['host'],
                            port=config['port'])

def exec_sql_file(path):
    full_path = os.path.join(os.path.dirname(__file__), f'../../{path}')
    conn = connect()
    cur = conn.cursor()
    with open(full_path, 'r') as file:
        cur.execute(file.read())
    conn.commit()
    conn.close()

def exec_get_one(sql, args={}):
    conn = connect()
    cur = conn.cursor()
    cur.execute(sql, args)
    one = cur.fetchone()
    conn.close()
    return one

def exec_get_all(sql, args={}):
    conn = connect()
    cur = conn.cursor()
    cur.execute(sql, args)
    # https://www.psycopg.org/docs/cursor.html#cursor.fetchall
    list_of_tuples = cur.fetchall()
    conn.close()
    return list_of_tuples

def exec_commit(sql, args={}):
    conn = connect()
    cur = conn.cursor()
    result = cur.execute(sql, args)
    conn.commit()
    conn.close()
    return result

def exec_commit_get_one(sql, args={}):
    """Note: Only works with an SQL RETURNING statement"""
    conn = connect()
    cur = conn.cursor()
    cur.execute(sql, args)
    postgresql_returning = cur.fetchone()
    if (postgresql_returning != None):
        postgresql_returning = postgresql_returning[0]
    conn.commit()
    conn.close()
    return postgresql_returning

def exec_commit_get_all(sql, args={}):
    conn = connect()
    cur = conn.cursor()
    cur.execute(sql, args)
    postgresql_returning = cur.fetchall()
    conn.commit()
    conn.close()
    return postgresql_returning

def exec_list(sql, list = {}):
    conn = connect()
    cur = conn.cursor()
    result_list = []
    for data_item in list:
        cur.execute(sql, data_item)
        new_id = cur.fetchone()[0]
        result_list.append(new_id)
    conn.commit()
    conn.close()

    return result_list

