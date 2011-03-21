import mail
import models
import re
import tornado.web


class BaseRequestHandler( tornado.web.RequestHandler ):
    def current_user( self ):
        return models.User.lookup( self.get_secure_cookie("user") or str(self.request.remote_ip) )


            
class signin( BaseRequestHandler ):
    def get( self ):
        self.render("signin.html", q="")
    def post( self ):
        email = self.get_argument("email")
        password = self.get_argument("password")
        try:
            user = models.signin( email, password )
            self.set_secure_cookie("user",user.email)
            self.redirect("/recent")
        else:
            self.redirect("/signin?error=signin")



class signout( BaseRequestHandler ):
    def get( self ):
        self.clear_cookie("user")
        self.redirect("/signin")



RE_EMAIL    = re.compile(r"^[-a-z0-9_]+@([-a-z0-9]+\.)+[a-z]{2,6}$",re.IGNORECASE)
class signup( BaseRequestHandler ):
    def get( self ):
        self.render("signup.html", q="")
    def post( self ):
        email = self.get_argument("email")
        password = self.get_argument("password")
        if not RE_EMAIL.match(email): 
           return self.redirect("/signup?error=email")
        try:
            user = models.signup( email, password )
            mymail.confirm_signup( user.email )
            self.redirect("/signin")
        except:
            self.redirect("/signin?error=duplicate_signup")



class index( BaseRequestHandler ):
    def get( self ):
        self.render("index.html")



class player( BaseRequestHandler ):
    def get( self ):
        v = self.get_argument("v",None)
        q = self.get_argument("q","")
        if v==None:
            if q=="":
                q = self.current_user.recommend_query()
            v = self.current_user.recommend_video(q)
            self.redirect( "/player?v=%s&q=%s" % (v.id,tornado.escape.url_escape(q)) )
        else:
            self.render( "player.html", v=v, q=q )



