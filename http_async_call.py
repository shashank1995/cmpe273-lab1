import grequests

responses = (grequests.get('https://webhook.site/d7ccff35-3363-4661-9e4a-de1319def319') for a in range(50))

all_responses = grequests.map(responses)
all_responses_date = []
for response in all_responses:
	print(response.headers['Date'])
	all_responses_date.append(response.headers['Date'])

count = {}
different_response = []
for response in all_responses_date:
	if response not in different_response:
		different_response.append(response)
		count[response] = 1
	else:
		count[response] = count[response] + 1

#Response frequency with respect to time
for different_responses in different_response:
	print("Response with date: %s has count of %d" % (different_responses,count[different_responses]))