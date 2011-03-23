import tornado.web
import tornado.database

db = tornado.database(
    host="localhost", database="mengomengo",
    user="root", password="mengomengo", 
)



class BaseHandler( tornado.web.RequestHandler ):
    def current_user( self ):
        return self.secure_cookie('user')


    
class index( tornado.web.RequestHandler ):
    def get( self ):
        self.redirect("/connect")



class connect( tornado.web.RequestHandler ):
    def get( self ):
        self.render("connect.html")



class myfeed( tornado.web.RequestHandler ):
    def get( self ):
        self.render("myfeed.html")


