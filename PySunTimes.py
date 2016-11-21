"""This program takes the name of a city as input from the user and returns sunrise and sunset times.
Calculation taken from here:
https://en.wikipedia.org/wiki/Sunrise_equation#Complete_calculation_on_Earth
"""
import datetime
import math
import requests

def julianDay(date=None):
	"""Returns current Julian date"""

	# calculate equation terms
	if date is None: date = datetime.datetime.now() # get today's date and time
	year = date.year
	month = date.month
	day = date.day
	hour = date.hour
	min = date.minute
	sec = date.second
	a = math.floor((14-month)/12)
	y = year + 4800 - a
	m = month + 12*a - 3

	J = day + math.floor((153*m + 2)/5) + (365*y) + math.floor(y/4) - math.floor(y/100) + math.floor(y/400) - 32045

	return J

def getLon(city):
	"""Returns given city's West longitude using Google Maps geocoding API"""

	response = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address={}".format(city)) 
	responseJSON = response.json()
	lon = responseJSON['results'][0]['geometry']['location']['lng']

	return abs(lon)


def meanSolar():
	"""Returns mean solar time"""