import re
import tornado.web
import tornado.database


db = tornado.database.Connection(
    host="localhost", database="mengomengo",
    user="root", password="mengomengo", 
)

re_fbid = re.compile("access_token=(?P<tk>.*)")
class BaseRequestHandler( tornado.web.RequestHandler ):
    def get_current_user( self ):
	raise Exception( self.get_cookie("fbs_204128796282802") )        
	return re_fbid.match(self.get_cookie("fbs_204128796282802")).group(0)        
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
            news = db.query("select v.* from stalking as s,list as l,video as v "
                "on s.victim=l.id and l.id=v.list"
                "where s.stalker=%s "
                "order by v.created_at", self.current_user)
            self.render("wall.html", news=news )
        else:
            self.render("connect.html")

class lists( BaseRequestHandler ):
    def get( self ):
        user = self.get_argument("user",self.current_user)
        self.render("lists.html")

class friends( BaseRequestHandler ):
    def get( self ):
        self.render("friends.html")

class player( BaseRequestHandler ):
    @tornado.web.authenticated
    def get( self ):
        v = self.get_argument("v")
        video = db.get("select list.title as list, list.id as list_id, video.title as title, video.id as video_id, type,data "
                       "from video,list where video.list=list.id and video.id=%s", v)
        prev = None
        next = None
        found = False
        for v in db.query("select id from video where list=%s",video.list_id):
            if found: next = v.id; break
            if v.id == video.video_id: found = True
            else: prev = v.id
        self.render("player.html", video=video, prev=prev, next=next)


class upload( BaseRequestHandler ):
    @tornado.web.authenticated
    def get( self ):
        self.render("upload.html")

class about( BaseRequestHandler ):
    @tornado.web.authenticated
    def get( self ):
        self.render("about.html")

class blog( BaseRequestHandler ):
    @tornado.web.authenticated
    def get( self ):
        self.render("blog.html")

class contact( BaseRequestHandler ):
    @tornado.web.authenticated
    def get( self ):
        self.render("contact.html")

class copyright( BaseRequestHandler ):
    @tornado.web.authenticated
    def get( self ):
        self.render("copyright.html")

class privacy( BaseRequestHandler ):
    @tornado.web.authenticated
    def get( self ):
        self.render("privacy.html")

class terms( BaseRequestHandler ):
    @tornado.web.authenticated
    def get( self ):
        self.render("terms.html")
