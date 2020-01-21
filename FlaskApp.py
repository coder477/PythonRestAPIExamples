'''
Created on 30-Sep-2019

@author: sneha
'''
from flask import Flask
from flask_restful import Resource, Api, reqparse
import service as service
import json
from gevent.pywsgi import WSGIServer



app=Flask(__name__)
api=Api(app)
parser = reqparse.RequestParser()
class GetHandler(Resource):
    def get(self,id):
        service.getitem(id)
        return (json.loads( json.dumps(service.getitem(id))))
        
class PostHandler(Resource):
    def post(self):     
        parser.add_argument('name', type=str, required=True)
        args=parser.parse_args()
        name=args['name']
        result=service.savetodb(name)
        return ({'result':result})
        
        
api.add_resource(GetHandler,"/apif/get/<id>")
api.add_resource(PostHandler,"/apif/data")

  
if __name__ == '__main__':
    #app.run(port=5000)
    """use gevent for while deploying in prod"""
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()