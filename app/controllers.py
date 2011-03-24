import tornado.web
import tornado.database

db = tornado.database.Connection(
    host="localhost", database="mengomengo",
    user="root", password="mengomengo", 
)



class index( tornado.web.RequestHandler ):
    def get( self ):
        if False:
            self.render("wall.html")
        else:
            self.render("connect.html")




