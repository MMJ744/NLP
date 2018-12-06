import re
def save_tagged_data(data, entities, number):
	tagged_data = ""
	for part, items in entities.items():
		for item in items:
			data = re.sub(item, '<' + part + '>\\g<0></' + part + '>', data)
	# file = open("output/" + str(number) + ".txt")
	# file.write(data)
	# file.close()
	return data


def equal_time(time1, time2):
	t1 = time1
	t2 = time2
	print(t1 + "---" + t2)
	if t1 == t2:
		return True
	t1 = re.sub(':00', '',t1)
	t2 = re.sub(':00','',t2)
	print(t1 + "---" + t2)
	regx = '\s?[AaPp].?[mM]'
	t1 = re.sub(regx,'',t1)
	t2 = re.sub(regx, '', t2)
	print(t1 + "---" + t2)
	return int(t1)==int(t2)

def sort_times(times, extra_times):
	stime = ""
	etime = ""
	for a, b, c in times:
		if a != '':
			stime = a
			etime = b
		if c != '': stime = c
	stimes = set()
	etimes = set()
	for time in extra_times:
		if equal_time(time, stime): stimes.add(time)
		if equal_time(time, etime): etimes.add(time)
	return (stimes, etimes)

def tag_regex_data(data):
	tregx = '(?:[0-2]?[0-9]:[0-5][0-9](?:\s?(?:AM|PM|am|pm))?)|(?:[0-2]?[0-9]\s?(?:[AaPp].?[mM]))'
	patterns = {
		'time': '(?:Time:\s*)('+tregx+')\s*-\s*('+tregx+')|(?:Time:\s*)('+tregx+')',
		'sentence': '[A-Z][^\.\!\?]*[\.\!\?](?:(?=\s)|"\s+[a-z][^\.\!\?]*[\.\!\?]|[A-z][^\.\!\?]*[\.\!\?]|)'
	}
	entities = dict()
	for key, pattern in patterns.items():
		entities[key] = (re.findall(pattern, data))
	entities['sentence'] = [x[:-1] for x in entities['sentence']]
	times = entities.pop('time')
	print(times)
	extra_times = re.findall(tregx,data)
	print(extra_times)
	stimes, etimes = sort_times(times, extra_times)
	print(stimes)
	print(etimes)
	return entities

s = 'Brett said "hello" to me. And I dont know whats happening but "Why is it doing this!" is bad.'
t = 'Time:     1:00 PM - 3PM          fhniiieh \n etjeikjfi 16:54 jfeijf \n 1pm'
print(tag_regex_data(t))

