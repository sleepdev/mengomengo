import tornado.web
import tornado.database

db = tornado.database.Connection(
    host="localhost", database="mengomengo",
    user="root", password="mengomengo", 
)

class BaseRequestHandler( tornado.web.RequestHandler ):
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


class api_wallpost( BaseRequestHandler ):
    def get( self ):
        user = self.get_argument("user")
        if self.has_permission("read",user,"wall"):
            start = self.get_argument("start",0)
            limit = self.get_argument("limit",20)
            data = db.query("select * from wallpost where user=%s limit %s,%s", user, start, limit)
            return self.write({"data": data})
    def post( self ): 
        user = self.get_argument("user")
        if self.has_permission("write",user,"wallpost"):
            url = self.get_argument("url")
            message = self.get_argument("message","")
            db.execute("insert wallpost(url,message) values(%s,%s)",url,message)
    def delete( self ): 
        user = self.get_argument("user")
        if self.has_permission("delete",user,"wallpost"):
            url = self.get_argument("url")
            db.execute("delete from wallpost where url=%s",url)
            


class api_subscription( BaseRequestHandler ):
    def get( self ):
        user = self.get_argument("user")
        if self.has_permission("read",user,"subscription"):
            start = self.get_argument("start",0)
            limit = self.get_argument("limit",20)
            data = db.query("select * from subscription where user=%s limit %s,%s", user, start, limit)
            return self.write({"data": data})
    def post( self ): 
        user = self.get_argument("user")
        if self.has_permission("write",user,"subscription"):
            playlist = self.get_argument("playlist")
            db.execute("insert subscription(playlist) values(%s)",playlist)
    def delete( self ): 
        user = self.get_argument("user")
        if self.has_permission("delete",user,"subscription"):
            playlist = self.get_argument("playlist")
            db.execute("delete from subscription where playlist=%s",playlist)



class api_playlist( BaseRequestHandler ):
    def get( self ):
        user = self.get_argument("user")
        if self.has_permission("read",user,"playlist"):
            start = self.get_argument("start",0)
            limit = self.get_argument("limit",20)
            data = db.query("select * from playlist where user=%s limit %s,%s", user, start, limit)
            return self.write({"data": data})
    def post( self ): 
        user = self.get_argument("user")
        if self.has_permission("write",user,"playlist"):
            title = self.get_argument("title")
            db.execute("insert playlist(title) values(%s)",title)
    def delete( self ): 
        user = self.get_argument("user")
        if self.has_permission("delete",user,"wallpost"):
            title = self.get_argument("title")
            #TODO, delete iff playlist is empty
            db.execute("delete from playlist where title=%s",title)



class api_video( BaseRequestHandler ):
    def get( self ):
        playlist = self.get_argument("playlist")
        if self.has_permission("read",playlist,"video"):
            start = self.get_argument("start",0)
            limit = self.get_argument("limit",20)
            data = db.query("select * from video where playlist=%s limit %s,%s", playlist, start, limit)
            return self.write({"data": data})
    def post( self ): 
        playlist = self.get_argument("playlist")
        if self.has_permission("write",playlist,"video"):
            url = self.get_argument("url")
            db.execute("insert wallpost(url) values(%s)",url)
    def delete( self ): 
        playlist = self.get_argument("playlist")
        if self.has_permission("delete",playlist,"wallpost"):
            url = self.get_argument("url")
            db.execute("delete from wallpost where url=%s",url)
