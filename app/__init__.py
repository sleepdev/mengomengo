
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
    ( "/friends",                   controllers.friends          ),
    ( "/lists",                     controllers.lists            ),
    ( "/player",                    controllers.player           ),
    ( "/upload",                    controllers.upload           ),

    ( "/about",                     controllers.about            ),
    ( "/blog",                      controllers.blog             ),
    ( "/contact",                   controllers.contact          ),
    ( "/copyright",                 controllers.copyright        ),
    ( "/privacy",                   controllers.privacy          ),
    ( "/terms",                     controllers.terms            ),

], **settings )



tornado.httpserver.HTTPServer(application, xheaders=True ).listen( 80 )
tornado.ioloop.IOLoop.instance().start()


