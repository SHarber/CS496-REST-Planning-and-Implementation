#********************************************
# Author: Sarah Harber
# CS 496 Mobile & Cloud Development
#********************************************

from google.appengine.ext import nbd
import webapp2
import json

# Slip Class
class Slip(nbd.model):
	number = nbd.IntegerProperty(required=True)
	current_boat = nbd.StringProperty(required=True)
	arrival_date = nbd.StringProperty(required=True)
	
