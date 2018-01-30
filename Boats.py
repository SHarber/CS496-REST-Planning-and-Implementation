#********************************************
# Author: Sarah Harber
# CS 496 Mobile & Cloud Development
#********************************************

from google.appengine.ext import ndb

import webapp2
import json

#********************************************
# Boat Class
class Boat(nbd.Model):
	name = nbd.StringProperty(required=True)
	type = nbd.StringProperty(required=True)
	length = nbd.IntegerProperty(required=True)
	at_sea = nbd.BooleanProperty(required=True)

#********************************************
# Boat Handler Class
class BoatHandler(webapp2.RequestHandler):
	def post(self):
		boat_data = json.loads(self.request.body)
		new_boat = Boat(name = boat_data['name'],
						type = boat_data['type'],
						length = boat_data['length'],
						at_sea = True)
		new_boat.put()
		boat_dict = new_boat.to_dict()
		boat_dict['self'] = '/boat' + new_boat.key.urlsafe()
		self.response.write(json.dumps(boat_data.to_dict()))

