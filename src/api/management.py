from flask_restful import Resource, reqparse, request  #NOTE: Import from flask_restful, not python
from db.db_utils import *

from db.dnd import rebuild_tables

class Init(Resource):
    def post(self):
        rebuild_tables()

class Version(Resource):
    def get(self):
        return (exec_get_one('SELECT VERSION()'))