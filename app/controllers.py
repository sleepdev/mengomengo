import tornado.web
import tornado.database

db = tornado.database.Connection(
    host="localhost", database="mengomengo",
    user="root", password="mengomengo", 
)

class BaseHandler( BaseRequestHandler ):
    def get_current_user( self ):
	return self.get_cookie("fbs_204128796282802")
    def has_permisison( self, verb, owner, object ):
        authorized = True
        if not authorized:
            self.write({
                "error": {
                    "type": "AuthException",
                    "message": "You are not permitted to %s the %s of the group having id=%s" % (verb, object, owner)
                }
            })
        return authorized

class index( BaseRequestHandler ):
    def get( self ):
        if self.current_user:
            self.render("wall.html")
        else:
            self.render("connect.html")


class api_wall( BaseRequestHandler ):
    def get( self ):
        user = self.get_argument("user")
        if self.has_permission("read",user,"wall"):
            start = self.get_argument("start",0)
            limit = self.get_argument("limit",20)
            data = db.query("select * from wall where user=%s limit %s,%s", user, start, limit)
            return self.write({"data": data})
    def post( self ): 
        pass
    def delete( self ): 
        pass



class api_subscriptions( BaseRequestHandler ):
    def get( self ):
        user = self.get_argument("user")
        if self.has_permission("read",user,"subscriptions")
            start = self.get_argument("start",0)
            limit = self.get_argument("limit",20)
            data = db.query("select * from subscriptions where user=%s limit %s,%s", user, start, limit)
            return self.write({"data": data})
    def post( self ):
        pass
    def delete( self ):
        pass



class api_playlists( BaseRequestHandler ):
    def get( self ):
        user = self.get_argument("user")
        if self.has_permission("read",user,"playlists")
            start = self.get_argument("start",0)
            limit = self.get_argument("limit",20)
            data = db.query("select * from playlists where user=%s limit %s,%s", user, start, limit)
            return self.write({"data": data})
    def post( self ):
        pass
    def delete( self ):
        pass



class api_videos( BaseRequestHandler ):
    def get( self ):
        playlist = self.get_argument("playlist")
        if self.has_permission("read",playlist,"videos")
            start = self.get_argument("start",0)
            limit = self.get_argument("limit",20)
            data = db.query("select * from videos where playlist=%s limit %s,%s", playlist, start, limit)
            return self.write({"data": data})
    def post( self ):
        pass
    def delete( self ):
        pass
