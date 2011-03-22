import tornado.web


            
class index( tornado.web.RequestHandler ):
    def get( self ):
        self.redirect("/connect")



class connect( tornado.web.RequestHandler ):
    def get( self ):
        self.render("connect.html")



class myfeed( tornado.web.RequestHandler ):
    def get( self ):
        self.render("myfeed.html")
