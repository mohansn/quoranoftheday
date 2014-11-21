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
     <meta name=viewport content="width=device-width, initial-scale=1">
     <title> Quoran Of The Day </title>
     <script src="js/jquery-2.1.1.min.js"></script>

     <!-- Latest compiled and minified CSS -->
     <link rel="stylesheet" href="stylesheets/bootstrap.min.css">

     <!-- Optional theme -->
     <link rel="stylesheet" href="stylesheets/bootstrap-theme.min.css">

     <!-- Latest compiled and minified JavaScript -->
     <script src="js/bootstrap.min.js"></script>

     <link rel="shortcut icon" type="image/x-icon" href="favicon.ico">
     <link rel="stylesheet" type="text/css" href="stylesheets/chart.css">
     <link rel="stylesheet" type="text/css" href="stylesheets/mainpage.css">
   </head>
    <body>
    <script src="js/d3.min.js" charset="utf-8"></script>
    <script src="js/d3pie.min.js"></script>
    <script src="js/pie.js"></script>
    <script src="js/main.js"></script>
    <div class="headerdiv">
      <h1>
        Stats on Quorans of the Day!
      </h1>
    </div>
      <form class="form-horizontal">
        <fieldset>

          <!-- Form Name -->
          <legend>Quoran Of The Day</legend>

          <!-- Select Basic -->
          <div class="control-group">
            <label class="control-label" for="selectbasic">Who?</label>
            <div class="controls">
              <select id="nameselect" name="nameselect" class="input-xlarge">
"""
""" FIXME: Convert to use of jinja2 or other template system """
for name in names:
    MAIN_PAGE_HTML = MAIN_PAGE_HTML + "<option value=\"" + name + "\"> " + name + "</option>"

MAIN_PAGE_HTML = MAIN_PAGE_HTML + """
              </select>
            </div>
          </div>

          <!-- Button -->
          <div class="control-group">
            <label class="control-label" for="singlebutton"></label>
            <div class="controls">
              <button id="nameinput" name="nameinput" class="btn btn-success">Get me some pie!</button>
            </div>
          </div>
        </fieldset>
      </form>
    </body>
  </html>
"""

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
