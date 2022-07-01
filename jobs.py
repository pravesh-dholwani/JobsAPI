from flask_restful import Resource
import bs4,requests



class Jobs(Resource):
    def get(self,id):
