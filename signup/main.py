import os
import webapp2
import jinja2


from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'template')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                               autoescape=True)


class Handler(webapp2.RequestHandler):
    def write(self, *a, **kwargs):
        self.response.out.write(*a, **kwargs)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kwargs):
        self.write(self.render_str(template, **kwargs))



class UserData(db.Model):
    username = db.StringProperty(required = True)
    password = db.StringProperty(required = True)
    email = db.StringProperty


class RegisterPageHandler(Handler):
    def render_main(self, username = "", email=""):
        flag=0
        data = db.GqlQuery("SELECT * FROM UserData")
        for i in data:
            if username == i.username:
                flag=1
        if flag!=0:

            error4 = "This username already exists"
            self.render("register.html", error4=error4, email=email)
        else:

            self.write("Thanks for the registration")

    def get(self):
        self.render("register.html")

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        verify_password = self.request.get('verify')
        email = self.request.get('email')
        if username and password and verify_password or email:
            if password == verify_password:
                b=UserData(username=username, password=password, email=email)
                b.put()
                self.render_main(username)
            else:
                error1 = "password does not matches with the verify password"
                self.render("register.html", username=username, email=email, error1=error1)

        else:
            error2 = "That wasn't a correct username"
            error3 = "That wasn't a correct password"
            self.render("register.html", error2 = error2, error3=error3)

app = webapp2.WSGIApplication([
    ('/', RegisterPageHandler)], debug=True)