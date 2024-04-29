from flask_restful import Resource, reqparse, request  #NOTE: Import from flask_restful, not python
from db.db_utils import *

class Init(Resource):
    def post(self):
        rebuild_test_tables()

class Version(Resource):
    def get(self):
        return (exec_get_one('SELECT VERSION()'))