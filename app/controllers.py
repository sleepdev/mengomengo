import tornado.web
import tornado.database

db = tornado.database.Connection(
    host="localhost", database="mengomengo",
    user="root", password="mengomengo", 
)

class BaseRequestHandler( tornado.web.RequestHandler ):
    def get_current_user( self ):
	return self.get_cookie("fbs_204128796282802")
    def has_permission( self, verb, owner, object ):
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

class player( BaseRequestHandler ):
    @tornado.web.authenticated
    def get( self ):
        v = self.get_argument("v")
        video = db.get("select (list.title as list, title, type, data) from video,list where video.list=list.id and video.id=%s", v)
        prev = None
        next = None
        self.render("player.html", video=video, prev=prev, next=next)



