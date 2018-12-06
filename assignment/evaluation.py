import re


def extract_sem_info(data):
	patterns = {
		'stime': '<stime>(.*?)</stime>',
		'etime': '<etime>(.*?)</etime>',
		'speaker': '<speaker>(.*?)</speaker>',
		'location': '<location>(.*?)</location>',
		'sentence': '<sentence>(.*?)</sentence>',
		'paragraph': '<paragraph>(.*?)</paragraph>'
	}
	entities = dict()
	for key, value in patterns.items():
		entities[key] = set(re.findall(value, data))
	return entities

def eval_all():
	pres = []
	selfs = []
	for c in range(301, 485):  # 485
		file = open('data/test_tagged/' + str(c) + '.txt', 'r')
		pre = file.read()
		pres = pres + [extract_sem_info(pre)]
		file.close()
		file = open('output/' + str(c) + '.txt', 'r')
		self = file.read()
		selfs = selfs + [extract_sem_info(self)]
		file.close()
	return evaluate_tagging(pres, selfs)


def evaluate_correct(pretagged, selftagged):
	correct_dict = dict()
	correct_total = 0
	for part, items in selftagged.items():
		correct = pretagged[part]
		correct_count = 0
		for entity in correct:
			if entity in items:
				correct_count = correct_count + 1
				correct_total = correct_total + 1
		correct_dict[part] = correct_count
	correct_dict['total'] = correct_total
	return correct_dict


def count_entities(x):
	counts = dict()
	c = 0
	for part, items in x.items():
		counts[part] = len(items)
		c = c + len(items)
	counts['total'] = c
	return counts


def add_dict(x, y):
	for key, value in y.items():
		x[key] = x[key] + y[key]


def evaluate_tagging(pretagged, selftagged):
	correct_dict = {'stime': 0, 'etime': 0, 'speaker': 0, 'location': 0, 'sentence': 0, 'topic': 0, 'paragraph': 0,
	                'total': 0}
	pre_totals = correct_dict.copy()
	self_totals = correct_dict.copy()
	for c in range(0, len(pretagged)):
		add_dict(correct_dict, evaluate_correct(pretagged[c], selftagged[c]))
		add_dict(pre_totals, count_entities(pretagged[c]))
		add_dict(self_totals, count_entities(selftagged[c]))
	evaluation = dict()
	print(pre_totals)
	print(self_totals)
	for part, items in correct_dict.items():
		entity = dict()
		try:
			precision = correct_dict[part] / self_totals[part]
		except ZeroDivisionError:
			precision = 0
		entity['precision'] = precision
		try:
			recall = correct_dict[part] / pre_totals[part]
		except ZeroDivisionError:
			recall = 0
		entity['recall'] = recall
		try:
			Fmeasure = 2 * (precision * recall / (precision + recall))
		except ZeroDivisionError:
			Fmeasure = 0
		entity['Fmeasure'] = Fmeasure
		evaluation[part] = entity
	return evaluation


x = '<speaker>Ramesh Bollapragada</speaker>, gdr <stime>1:00 PM</stime> Place:    <location>4623 WEAN HALL</location>'
y = '<speaker>Ramesh Bollapragada</speaker>, gdr <stime>1:00 PM</stime> Place:   '
#print(evaluate_tagging([extract_sem_info(x), extract_sem_info(x)], [extract_sem_info(y), extract_sem_info(y)]))
