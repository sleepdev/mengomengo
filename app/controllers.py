import tornado.web
import tornado.database

db = tornado.database.Connection(
    host="localhost", database="mengomengo",
    user="root", password="mengomengo", 
)



class index( tornado.web.RequestHandler ):
    def get( self ):
	authenticated = self.get_cookie("fbs_204128796282802")
        if authenticated:
            self.render("wall.html")
        else:
            self.render("connect.html")




