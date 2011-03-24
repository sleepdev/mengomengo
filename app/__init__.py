
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
)

application = tornado.web.Application( [
    ( "/",                          controllers.index       ),
    ( "/api/wallpost",              controllers.api_wallpost ),
    ( "/api/subscription",          controllers.api_subscription ),
    ( "/api/playlist",              controllers.api_playlist ),
    ( "/api/video",                 controllers.api_video ),
], **settings )



tornado.httpserver.HTTPServer(application, xheaders=True ).listen( 80 )
tornado.ioloop.IOLoop.instance().start()


