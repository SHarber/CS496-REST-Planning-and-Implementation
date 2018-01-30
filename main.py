from google.appengine.ext import ndb
import webapp2
import json

# Import User Created Classes
from boats import Boat, BoatHandler


class MainPage(webapp2.RequestHandler):

    def get(self):
       self.response.write("REST Planning and Implementation")


allowed_methods = webapp2.WSGIApplication.allowed_methods
new_allowed_methods = allowed_methods.union(('PATCH',))
webapp2.WSGIApplication.allowed_methods = new_allowed_methods
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/boats', BoatHandler),
    ('/fish/(.*)', BoatHandler)
], debug=True)
# [END app]