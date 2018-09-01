import requests
from datetime import datetime

r = requests.get("https://webhook.site/d7ccff35-3363-4661-9e4a-de1319def319")
print (r.headers['Date'])
r = requests.get("https://webhook.site/d7ccff35-3363-4661-9e4a-de1319def319")
print (r.headers['Date'])
r = requests.get("https://webhook.site/d7ccff35-3363-4661-9e4a-de1319def319")
print (r.headers['Date'])


#Calculating average ping time
print ("Calculating average ping time:")
r = requests.get("https://webhook.site/d7ccff35-3363-4661-9e4a-de1319def319")
time1 = datetime.strptime(r.headers['Date'], '%a, %d %b %Y %H:%M:%S %Z')
print (r.headers['Date'])
r = requests.get("https://webhook.site/d7ccff35-3363-4661-9e4a-de1319def319")
time2 = datetime.strptime(r.headers['Date'], '%a, %d %b %Y %H:%M:%S %Z')
print (r.headers['Date'])
r = requests.get("https://webhook.site/d7ccff35-3363-4661-9e4a-de1319def319")
time3 = datetime.strptime(r.headers['Date'], '%a, %d %b %Y %H:%M:%S %Z')
print (r.headers['Date'])
r = requests.get("https://webhook.site/d7ccff35-3363-4661-9e4a-de1319def319")
time4 = datetime.strptime(r.headers['Date'], '%a, %d %b %Y %H:%M:%S %Z')
print (r.headers['Date'])

avg_ping_time = 0

#Considering Hour remain same even though I can take that testcase also
if time1.minute == time2.minute:
	avg_ping_time = (time2.second-time1.second)
else:
	minute_taken = (time2.minute-time1.minute)
	if minute_taken == 1:
		avg_ping_time = (time2.second + (60-time1.second))
	else:
		avg_ping_time = (minute_taken-1)*60
		avg_ping_time = avg_ping_time + (time2.second + (60-time1.second))

#Doing this same for two more cases so that I can find average ping time

if time2.minute == time3.minute:
	avg_ping_time = avg_ping_time + (time3.second-time2.second)
else:
	minute_taken = (time3.minute-time2.minute)
	if minute_taken == 1:
		avg_ping_time = avg_ping_time + (time3.second + (60-time2.second))
	else:
		avg_ping_time = avg_ping_time + (minute_taken-1)*60
		avg_ping_time = avg_ping_time + (time3.second + (60-time2.second))

if time3.minute == time4.minute:
	avg_ping_time = avg_ping_time + (time4.second-time3.second)
else:
	minute_taken = (time4.minute-time3.minute)
	if minute_taken == 1:
		avg_ping_time = avg_ping_time + (time4.second + (60-time3.second))
	else:
		avg_ping_time = avg_ping_time + (minute_taken-1)*60
		avg_ping_time = avg_ping_time + (time4.second + (60-time3.second))


avg_ping_time = avg_ping_time/3

print ("Note: So average ping time is %f seconds." % (avg_ping_time))