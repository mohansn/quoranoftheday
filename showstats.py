from google.appengine.api import users
import webapp2
import cgi
from genhtml import get_html

names = [l.rstrip("\n") for l in open('usernames.txt','r').readlines()]
usernames = [l.rstrip("\n") for l in open('users.txt','r').readlines()]

namedict = dict (zip (names, usernames))
datadir = "data/"
MAIN_PAGE_HTML = """
<html>
   <head>
     <link rel="shortcut icon" type="image/x-icon" href="favicon.ico">
     <style>
       h1 {
         color:blue;
         background-color:#E9BEF5;
         font-family:helvetica,arial,sans-serif;
         text-align:center;
         border:solid 2px;
         border-radius:10px;
       }
       .headerdiv {
         display:inline-block;
         float:center
       }
       .datachoice {
         display:none
       }
     </style>
   </head>
    <body>
    <div class="headerdiv">
      <h1>
        Stats on Quorans of the Day!
      </h1>
    </div>
      <form action="/datavis" method="post">
        <div>
            <select name="nameselect" id>
"""
for name in names:
    MAIN_PAGE_HTML = MAIN_PAGE_HTML + "<option value=\"" + name + "\"> " + name + "</option>"

MAIN_PAGE_HTML = MAIN_PAGE_HTML + "</select></div>"
MAIN_PAGE_HTML = MAIN_PAGE_HTML + """<div class="datachoice"><input type="radio" name="datakind" checked="checked" value="static">Static (updated on Sep 17 '14)<br>
<input type="radio" name="datakind" value="dynamic">Dynamically updated on request <strong>Can be quite slow or fail</strong></div>"""

MAIN_PAGE_HTML = MAIN_PAGE_HTML + """<div><input type="submit" value="Get Stats"></div></form> </body> </html>"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(MAIN_PAGE_HTML)

class ShowStats(webapp2.RequestHandler):
    def post(self):
        name = cgi.escape(self.request.get('nameselect'))
        if (cgi.escape(self.request.get('datakind')) == "static"):
            statfile = open(datadir + namedict[name]+'.html', 'r')
            if (statfile is not None):
                self.response.write (statfile.read())
                statfile.close ()
            else:
                self.response.write ("<html><body> <h1> No data file found </h1> </body></html>")
        else:
            self.response.write(get_html(namedict[name]))
        


application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/datavis', ShowStats),
], debug=True)
