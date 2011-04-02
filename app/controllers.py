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
        self.render("player.html", video={
            'group':'Itazura na Kiss', 
            'order':'Episode 65, part 2', 
            'title':'Naoki proposes!'
        } )









class api_wall( BaseRequestHandler ):
    def get( self ):
        return self.write({"data": [ {"text":"item 1"}, {"text":"item 2"} ] })
        user = self.get_argument("user",self.current_user)
        if self.has_permission("read",user,"wall"):
            start = self.get_argument("start",0)
            limit = self.get_argument("limit",20)
            data = db.query("select * from wall where user=%s limit %s,%s", user, start, limit)
            return self.write({"data": data})
    def post( self ): 
        user = self.get_argument("user")
        if self.has_permission("write",user,"wall"):
            subject = self.get_argument("subject")
            verb   = self.get_argument("verb")
            object = self.get_argument("object")
            db.execute("insert wall(user,subject,verb,object) values(%s,%s,%s,%s)",user,subject,verb,object)
    def delete( self ): 
        user = self.get_argument("user")
        if self.has_permission("delete",user,"wall"):
            id = self.get_argument("id")
            db.execute("delete from wall where user=%s and id=%s",user,id)
            


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
            list = self.get_argument("list")
            db.execute("insert subscription(list) values(%s)",list)
    def delete( self ): 
        user = self.get_argument("user")
        if self.has_permission("delete",user,"subscription"):
            list = self.get_argument("list")
            db.execute("delete from subscription where list=%s",list)



class api_list( BaseRequestHandler ):
    def get( self ):
        user = self.get_argument("user")
        if self.has_permission("read",user,"list"):
            start = self.get_argument("start",0)
            limit = self.get_argument("limit",20)
            data = db.query("select * from list where user=%s limit %s,%s", user, start, limit)
            return self.write({"data": data})
    def post( self ): 
        user = self.get_argument("user")
        if self.has_permission("write",user,"list"):
            title = self.get_argument("title")
            db.execute("insert list(title) values(%s)",title)
    def delete( self ): 
        user = self.get_argument("user")
        if self.has_permission("delete",user,"wall"):
            title = self.get_argument("title")
            #TODO, delete iff playlist is empty
            db.execute("delete from list where title=%s",title)



class api_video( BaseRequestHandler ):
    def get( self ):
        list = self.get_argument("list")
        if self.has_permission("read",list,"video"):
            start = self.get_argument("start",0)
            limit = self.get_argument("limit",20)
            data = db.query("select * from video where list=%s limit %s,%s", playlist, start, limit)
            return self.write({"data": data})
    def post( self ): 
        list = self.get_argument("list")
        if self.has_permission("write",list,"video"):
            url = self.get_argument("url")
            title = self.get_argument("title")
            db.execute("insert video(list,url,title) values(%s,%s,%s)",list,url,title)
    def delete( self ): 
        list = self.get_argument("list")
        if self.has_permission("delete",list,"video"):
            url = self.get_argument("url")
            db.execute("delete from video where list=%s and url=%s",list,url)
