
import controllers

import tornado.web
import tornado.httpserver
import tornado.ioloop

import sys


settings = dict(
   cookie_secret  =  "DFT&GY*UHJ76879u0i&^%*TY&(H*U)J&^T*GY&HU(F&T",
   static_path    = os.path.join(os.path.dirname(__file__), "static"),
   template_path  = os.path.join(os.path.dirname(__file__), "views"),
)

application = tornado.web.Application( [
    ( "/",                          controllers.index       ),
    ( "/connect",                   controllers.connect     ),
], **settings )



#requires one command line argument, specifying the port to run on 
if __name__ == "__main__":
   assert len(sys.argv)==2 

   http_server = tornado.httpserver.HTTPServer(application, xheaders=True )

   listen_port = int(sys.argv[1])
   http_server.listen( listen_port )

   tornado.ioloop.IOLoop.instance().start()


