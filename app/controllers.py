import tornado.web
import tornado.database

db = tornado.database.Connection(
    host="localhost", database="mengomengo",
    user="root", password="mengomengo", 
)



class index( tornado.web.RequestHandler ):
    def get( self ):
        raise self.cookies
	access_token = self.get_cookie("access_token")
        if access_token:
            self.render("wall.html")
        else:
            self.render("connect.html")




