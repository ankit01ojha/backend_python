import os
import webapp2
import jinja2
from hashing import *

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


class MainPageHandler(Handler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        visits = 0
        visits_cookie_str = str(self.request.cookies.get('visits'))
        if visits_cookie_str:

            cookie_val = check_secure_val(visits_cookie_str)

            if cookie_val:
                visits = int(cookie_val)

        visits+=1
        new_cookie_val = make_secure_val(str(visits))


        self.response.headers.add_header('Set-Cookie', 'visits=%s' % new_cookie_val)
        self.write("You have visited this site %s times" % visits)



app = webapp2.WSGIApplication([
    ('/', MainPageHandler)], debug=True)