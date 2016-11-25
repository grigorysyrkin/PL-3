import requests
import json
import datetime
from time import time

timeBeg = time()
timeEnd = timeBeg + 604800
city = 'Boston'

URL = requests.get('https://api.meetup.com/2/open_events?and_text=False&country=us&offset=0&city='+city+'&format=json&limited_events=False&state=ma&photo-host=public&page=20&time='+str(int(timeBeg))+'000'+'%2C'+str(int(timeEnd))+'000'+'&radius=25.0&category=2&desc=False&status=upcoming&sig_id=216991390&sig=9280fca9fa17878243ebe6724cf31f59763c0ccf&key=28622f79165d7236e367e6317536')

URLdict = URL.json()

schedule = []
cnt = -1
for item1 in URLdict['results']:
	cnt += 1
	schedule.append([])
	schedule[cnt].append(item1['time'])
	if 'group' in item1:
		schedule[cnt].append(item1['group']['name'])
	if 'description' in item1:
		schedule[cnt].append(item1['description'][:150])
	if 'venue' in item1:
		schedule[cnt].append(item1['venue']['address_1'])

timeBeg2 = timeBeg

Html_file = open("index.html","w")
for i in range(7):
	timeBeg2 += 86400
	print('Day' + str(i + 1))
	Html_file.write('<b>Day</b>' + str(i + 1) + '\n' + '<br></br>')
	for j in range(len(schedule)):
		if schedule[j][0] in range(int(timeBeg2)*1000, (int(timeBeg2) + 86400)*1000):
			schedule[j][0] = int(schedule[j][0])
			schedule[j][0] = datetime.datetime.fromtimestamp(schedule[j][0]/1000)
			outp = str(schedule[j][0]) + '<br></br>' + str(schedule[j][1]) +  ' , ' + str(schedule[j][2])
			try:
				outp += schedule[j][3]
			except: pass
			print(outp)
			Html_file.write(outp + '<br></br><br></br><br></br>')
	print()
	Html_file.write('<br></br>')

Html_file.close()