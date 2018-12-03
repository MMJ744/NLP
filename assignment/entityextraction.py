import re


def extract_stuff(data):
    regex = {
        'stime': '<stime>(.*?)<stime>',
        'etime': '<etime>(.*?)<etime>',
        'speaker': '<speaker>(.*?)<speaker>',
        'location': '<location>(.*?)<location>',
        'sentence': '<sentence>(.*?)<sentence>',
        'topic': '<topic>(.*?)<topic>'
    }
    extracted_entities = dict()
    for entity in regex.keys():
        extracted_entities[entity] = re.findall(r'' + regex[entity], data)
    return extracted_entities


test = "<sentence>hi my name is bob<sentence>yep it is me<speaker>bob<speaker>yep"
print(extract_stuff(test))
