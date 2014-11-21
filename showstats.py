from google.appengine.api import users
import webapp2
import cgi
import urllib
from genhtml import get_html, get_topic_data_json

names = [l.rstrip("\n") for l in open('usernames.txt','r').readlines()]
usernames = [l.rstrip("\n") for l in open('users.txt','r').readlines()]

namedict = dict (zip (names, usernames))
datadir = "data/"
MAIN_PAGE_HTML = """
<html>
   <head>
     <title> Quoran Of The Day </title>
     <link rel="shortcut icon" type="image/x-icon" href="favicon.ico">
     <link rel="stylesheet" type="text/css" href="stylesheets/chart.css">
     <link rel="stylesheet" type="text/css" href="stylesheets/bootstrap-readable.min.css">
     <link rel="stylesheet" type="text/css" href="stylesheets/mainpage.css">
     <script src="js/jquery-2.1.1.min.js"></script>
     <script src="js/d3.min.js" charset="utf-8"></script>
     <script src="js/nv.d3.min.js" charset="utf-8"></script>
   </head>
    <body>
    <script src="js/d3pie.min.js"></script>
    <script src="js/pie.js"></script>
    <script src="js/main.js"></script>
    <div class="headerdiv">
      <h1>
        Stats on Quorans of the Day!
      </h1>
    </div>
      <form>
        <div>
            <select id="nameselect" name="nameselect">
"""

""" FIXME: Convert to use of jinja2 or other template system """
for name in names:
    MAIN_PAGE_HTML = MAIN_PAGE_HTML + "<option value=\"" + name + "\"> " + name + "</option>"

MAIN_PAGE_HTML = MAIN_PAGE_HTML + "</select></div>"
MAIN_PAGE_HTML = MAIN_PAGE_HTML + """<div><input id="nameinput" type="submit" value="Get Stats"></div></form> </body> </html>"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(MAIN_PAGE_HTML)

class GetData(webapp2.RequestHandler):
    def get (self):
        name = cgi.escape(self.request.get('user'))
        return self.response.write(get_topic_data_json(namedict[name]))



application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/getdata', GetData)
], debug=True)
