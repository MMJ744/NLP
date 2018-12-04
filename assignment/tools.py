import re

def extract_sem_info(data):
    regex = {
        'stime': '<stime>(.*?)</stime>',
        'etime': '<etime>(.*?)</etime>',
        'speaker': '<speaker>(.*?)</speaker>',
        'location': '<location>(.*?)</location>',
        'sentence': '<sentence>(.*?)</sentence>',
        'topic': '<topic>(.*?)</topic>',
        'paragraph': '<paragraph>(.*?)</topic>',
        'sentence': '<sentence>(.*?)</sentence>'
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
            print(entity)
            print(items)
            if entity in items:
                correct_count = correct_count + 1
                correct_total = correct_total + 1
        correct_dict[part] = correct_count
    correct_dict['total'] = correct_total
    return correct_dict

def evaluate_tagging(pretagged, selftagged):
    correct_dict = evaluate_correct(pretagged, selftagged)
    print(selftagged.values())
    print(sum(selftagged.values()))
    print(pretagged.values())
    print(sum(pretagged.values()))
    precision = correct_dict['total'] / len(selftagged)
    print(precision)
    recall = correct_dict['total'] / len(pretagged)
    print(recall)
    Fmeasure = 2 * (precision*recall / (precision + recall))
    print(Fmeasure)


x = "<speaker>Ramesh Bollapragada</speaker>, <stime>2:00</stime>  Time:<stime>1:00 PM</stime> Place:    <location>4623 WEAN HALL</location>"
x2 = "hfhf<stime>2:30</stime> <stime>4:80</stime> <stime>2:80</stime>  eTime:<stime>1:00 PM</stime> Place:de <speaker>ehfhfh</speaker> <location>4623 WEAN HALL</location>"

y = extract_sem_info(x)
y2 = extract_sem_info(x2)
print(y)
print(y2)
print(evaluate_tagging(y,y2))
