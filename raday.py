import requests, os
from datetime import datetime

import datetime

from bs4 import BeautifulSoup


DIR_LOC = os.path.dirname(os.path.realpath("__file__"))


def parse_time(t):
	return "%s%s"%(t.strftime("%Y_%m_%d_%H_"),int(float(t.strftime("%M"))/10)*10)

def get_image(date_time,location):
	#url = "http://weather.gc.ca/cacheable/images/radar/layers_detailed/rivers/wkr_rivers.gif"
	url = "http://weather.gc.ca/data/radar/detailed/temp_image/WKR/WKR_PRECIP_RAIN_%s.GIF"%date_time
	file_name = "%s/radar_img/%s"%(location,url.split("/")[-1])
	if os.path.isfile(file_name):
		return False
	try:
		r = requests.get(url, stream=True)
		if r.status_code == 200:
			with open(file_name, 'wb') as f:
				for chunk in r:
					f.write(chunk)

			return file_name
		else:
			print "failed %s"%file_name
	except Exception, e:
		print e
		pass


def update_images():
	time_time = datetime.datetime.utcnow()

	for x in range(0,10):
		time_time = time_time - datetime.timedelta(minutes=10)
		get_image(parse_time(time_time),DIR_LOC)



def get_weather():
	url = "http://www.theweathernetwork.com/36-hour-weather-forecast/canada/ontario/toronto"
	r = requests.get(url)
	if r.status_code == 200:
		soup = BeautifulSoup(r.text, 'html.parser')
		
		print soup.find_all("div",{"class":"forecastitems"})
		# div_container = soup.find_all("div",{"class":"thirty-six-hrs-html"})[0]
		# div_column = soup.find_all("div",{"class":"thirtysix-hours-column"})
		# for col in div_column:
		# 	print "\n\n"
		# 	print col
		
	else:
		print "could not get weather data"

	#"thirty-six-hrs-html"

get_weather()




