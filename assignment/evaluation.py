import re


def extract_sem_info(data):
    regex = {
        'stime': '<stime>(.*?)</stime>',
        'etime': '<etime>(.*?)</etime>',
        'speaker': '<speaker>(.*?)</speaker>',
        'location': '<location>(.*?)</location>',
        'sentence': '<sentence>(.*?)</sentence>',
        'topic': '<topic>(.*?)</topic>',
        'paragraph': '<paragraph>(.*?)</topic>'
    }
    extracted_entities = dict()
    for entity in regex.keys():
        extracted_entities[entity] = re.findall(r'' + regex[entity], data)
    return extracted_entities


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


def evaluate_tagging(pretagged, selftagged):
    correct_dict = evaluate_correct(pretagged, selftagged)
    pre_totals = count_entities(pretagged)
    self_totals = count_entities(selftagged)
    evaluation = dict()
    for part, items in correct_dict.items():
        entity = dict()
        try:
            precision = correct_dict[part] / self_totals[part]
        except ZeroDivisionError:
            precision = 0
        print(precision)
        entity['precision'] = precision
        try:
            recall = correct_dict['total'] / pre_totals[part]
        except ZeroDivisionError:
            recall = 0
        print(recall)
        entity['recall'] = recall
        try:
            Fmeasure = 2 * (precision * recall / (precision + recall))
        except ZeroDivisionError:
            Fmeasure = 0
        entity['Fmeasure'] = Fmeasure
        print(Fmeasure)
        evaluation[part] = entity
    return evaluation