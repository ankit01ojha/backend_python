import os
import webapp2
import jinja2
from convertor import convert
from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'template')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                               autoescape=True)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kwargs):
        self.response.out.write(*a, **kwargs)

    def render_str(self, template, **params):
        t= jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kwargs):
        self.write(self.render_str(template, **kwargs))

class MainPageHandler(Handler):
    def get(self):

        self.render("convert.html")

    def post(self):
        newtext=""
        text = self.request.get('text')
        if text:
            newtext= convert(str(text))

        self.render("convert.html", text=newtext)





app = webapp2.WSGIApplication([
    ('/', MainPageHandler)
], debug=True)