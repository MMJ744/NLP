import re

def save_tagged_data(data, entities, number):
	tagged_data = ""
	for part, items in entities.items():
		for item in items:
			data = re.sub(item, '<' + part + '>\\g<0></' + part + '>', data)
	# file = open("output/" + str(number) + ".txt")
	# file.write(tagged_data)
	# file.close()
	pattern = '[0-9]+:[0-9]+|[0-9]+-[0-9]'
	#p = '\\b((?!=|\.).)+(.)\\b'
	#tagged_data = re.sub(p, "<sentence>\\g<0></sentence>", data)
	return data

def tag_regex_data(data):
	s = 'Brett said "hello" to me. And I dont know whats happening but "Why is it doing this!" is bad.'
	t = 'dfsg <user@host.com> dfg user@host.com dfg <user@host.com fgh user@host.com>'
	patterns = {
		'time': '(?:[0-2]?[0-9]:[0-5][0-9](?:\s?(?:AM|PM|am|pm))?)|(?:[0-2]?[0-9]\s?(?:AM|PM|am|pm))',
		'sentence': '[A-Z][^\.\!\?]*[\.\!\?](?:(?=\s)|"\s+[a-z][^\.\!\?]*[\.\!\?]|[A-z][^\.\!\?]*[\.\!\?]|)'
	}
	entities = dict()
	for key, pattern in patterns.items():
		entities[key] = (re.findall(pattern, s))
	print(entities)
	entities['sentence'] = [x[:-1] for x in entities['sentence']]
	print(entities)
tag_regex_data("")

