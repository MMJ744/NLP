import re, nltk
from nltk.tag.stanford import  StanfordPOSTagger, StanfordNERTagger
def save_tagged_data(data, entities, number):
	tagged_data = ""
	for part, items in entities.items():
		items = set(items)
		for item in items:
			pat = '(?!<'+part+'>)('+re.escape(item)+')(?!<\/'+part+'>)'
			data = re.sub(pat, '<' + part + '>\\g<0></' + part + '>', data)
	file = open("output/" + str(number) + ".txt", 'w')
	file.write(data)
	file.close()


def equal_time(time1, time2):
	regx = '\s?[AaPp].?[mM]|from|at|to|till|\s|:00'
	t1 = re.sub(regx,'',time1)
	t2 = re.sub(regx, '', time2)
	return t1 == t2


def sort_times(times, extra_times):
	stime = ""
	etime = ""
	a,b,c = times
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

def tag_data(data):
	entities = tag_regex_data(data)
	speakers = entities['speaker']
	#tagger = StanfordNERTagger('C:/Users/Matthew/stanford-ner-2018-10-16/classifiers/english.all.3class.distsim.crf.ser.gz')
	for speaker in speakers:
		if " and " in speaker:
			speakers.remove(speaker)
			for s in speaker.split(" and "):
				speakers.append(s)


	return entities


def remove_sentence_noise(data):
	data = data.split('Abstract:', 1)[1]
	pattern = '\n(?:\n|\s*--.*|\s*\n)'
	#data = re.sub(pattern,'',data)
	return data


def tag_regex_data(data):
	tregex = '(?:[0-2]?[0-9]:[0-5][0-9](?:\s?(?:[AaPp].?[mM]))?)|(?:[0-2]?[0-9]\s?(?:[AaPp]\.?[mM]))'
	patterns = {
		'time': '(?:Time:\s*)('+tregex+')\s*-\s*('+tregex+')|(?:Time:\s*)('+tregex+')',
		'sentence': '[A-Z][^\.\!\?]*[\.\!\?](?:(?=\s)|"\s+[a-z][^\.\!\?]*[\.\!\?]|[A-z][^\.\!\?]*[\.\!\?]|)',
		'location': '(?:Place|WHERE|Location)(?::\s*)(.*)',
		'speaker': '(?:Who|WHO|Speaker|SPEAKER)(?::\s*)([^,(\n/-]*)',
		'speaker2': '(?:Lecture by\s)([^,(\n]*)'
	}
	entities = dict()
	entities['sentence'] = nltk.sent_tokenize(remove_sentence_noise(data))
	#entities['sentence'] = re.findall(patterns['sentence'],remove_sentence_noise(data))
	entities['sentence'] = [x[:-1] for x in entities['sentence']]
	#for x in entities['sentence']:
	#	if x=='Dr': entities['sentence'].remove(x)
	entities['time'] = re.findall(patterns['time'], data)
	entities['location'] = re.findall(patterns['location'], data)
	entities['speaker'] = re.findall(patterns['speaker'], data)
	[entities['speaker'].append(x) for x in re.findall(patterns['speaker2'],data)]
	new_speak = []
	for s in entities['speaker']:
		if s.endswith(' '):
			new_speak.append(s[:-1])
		else: new_speak.append(s)
	entities['speaker'] = new_speak
	times = set(entities.pop('time'))
	extra_times = set(re.findall(tregex,data))
	singles = set(re.findall('(?:from|at|to|till|until)\s[0-9]\s',data))
	extra_times = extra_times.union(singles)
	stimes = set()
	etimes = set()
	for each in times:
		s, e = sort_times(each, extra_times)
		stimes = stimes.union(s)
		etimes = etimes.union(e)
	entities['stime'] = stimes
	entities['etime'] = etimes
	return entities