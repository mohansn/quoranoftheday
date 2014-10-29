from google.appengine.api import users
import webapp2
import cgi
import urllib
from genhtml import get_html, get_topic_data_json

names = [l.rstrip("\n") for l in open('usernames.txt','r').readlines()]
usernames = [l.rstrip("\n") for l in open('users.txt','r').readlines()]

namedict = dict (zip (names, usernames))
MAIN_PAGE_HTML = """
<html>
   <head>
     <link rel="shortcut icon" type="image/x-icon" href="favicon.ico">
     <script src="js/jquery-2.1.1.min.js"></script>
     <script src="js/main.js"></script>
     <style>
       h1 {
         color:blue;
         background-color:#E9BEF5;
         font-family:garamond,serif;
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
      <form>
        <div>
            <select id="nameselect" name="nameselect">
"""

""" FIXME: Convert to use of jinja2 or other template system """
for name in names:
    MAIN_PAGE_HTML = MAIN_PAGE_HTML + "<option value=\"" + name + "\"> " + name + "</option>"

MAIN_PAGE_HTML = MAIN_PAGE_HTML + "</select></div>"
MAIN_PAGE_HTML = MAIN_PAGE_HTML + """<div><input id="nameinput" type="submit" value="Get Stats"></div></form>

<script>
// Prevent the form from submitting
$( "form" ).submit(function( event ) {
    alert($("#nameselect").val());
   console.log($("#nameselect").val());
    $.ajax({
        url:"/getdata",
        type: 'get',
        data: {
            'user': $("#nameselect").val(),
            async:false
        },
        success: function (data) {
            alert ("Got data");
            console.log (data);
        }
    });
    event.preventDefault();
});

</script>

</body> </html>"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(MAIN_PAGE_HTML)

class GetData(webapp2.RequestHandler):
    def get (self):
        name = cgi.escape(self.request.get('user'))
        print "hahahahaaaa!! " + name + " HAHAHAHAHAAA!!!"
        return self.response.write(get_topic_data_json(namedict[name]))



application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/getdata', GetData)
], debug=True)
