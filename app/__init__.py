
import controllers
import os
import tornado.web
import tornado.httpserver
import tornado.ioloop
import sys
	


settings = dict(
   cookie_secret  =  "DFT&GY*UHJ76879u0i&^%*TY&(H*U)J&^T*GY&HU(F&T",
   static_path    = os.path.join(os.path.dirname(__file__), "static"),
   template_path  = os.path.join(os.path.dirname(__file__), "views"),
   login_url      = '/',
)

application = tornado.web.Application( [
    ( "/",                          controllers.index            ),
    ( "/player",                    controllers.player           ),
    ( "/api/wall",                  controllers.api_wall         ),
    ( "/api/subscription",          controllers.api_subscription ),
    ( "/api/list",                  controllers.api_list         ),
    ( "/api/video",                 controllers.api_video        ),
], **settings )



tornado.httpserver.HTTPServer(application, xheaders=True ).listen( 80 )
tornado.ioloop.IOLoop.instance().start()


