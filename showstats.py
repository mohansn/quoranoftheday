from google.appengine.api import users
import webapp2
import cgi

names = [l.rstrip("\n") for l in open('usernames.txt','r').readlines()]
usernames = [l.rstrip("\n") for l in open('users.txt','r').readlines()]

namedict = dict (zip (names, usernames))
MAIN_PAGE_HTML = """
<html>
    <body>
      <form action="/datavis" method="post">
        <div>
            <select name="nameselect" id>
"""
for name in names:
    MAIN_PAGE_HTML = MAIN_PAGE_HTML + "<option value=\"" + name + "\"> " + name + "</option>"

MAIN_PAGE_HTML = MAIN_PAGE_HTML + "</select></div>" + """<div><input type="submit" value="Get Stats"></div></form> </body> </html>"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(MAIN_PAGE_HTML)

class ShowStats(webapp2.RequestHandler):
    def post(self):
        name = cgi.escape(self.request.get('nameselect'))
        statfile = open(namedict[name]+'.html', 'r')
        if (statfile is not None):
            self.response.write (statfile.read())
            statfile.close ()
        


application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/datavis', ShowStats),
], debug=True)
