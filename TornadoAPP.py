'''
Created on 30-Sep-2019

@author: sneha
'''
from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
import json
import service as  service

class GetHandler(RequestHandler):
    def get(self,id):
        service.getitem(id)
        self.write(json.loads( json.dumps(service.getitem(id))))
        
class PostHandler(RequestHandler):
    def post(self):
        name=self.get_argument("name")
        result=service.savetodb(name)
        self.write({'result':result})

def make_app():
    urls = [("/api/get/([^/]+)?", GetHandler),
            ("/api/data",PostHandler)]
    return Application(urls,debug=True)
  
if __name__ == '__main__':
    app = make_app()
    app.listen(3000)
    IOLoop.instance().start()