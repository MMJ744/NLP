import re

def extract_sem_info(data):
    regex = {
        'stime': '<stime>(.*?)</stime>',
        'etime': '<etime>(.*?)</etime>',
        'speaker': '<speaker>(.*?)</speaker>',
        'location': '<location>(.*?)</location>',
        'sentence': '<sentence>(.*?)</sentence>',
        'topic': '<topic>(.*?)</topic>'
        'paragraph': '<paragraph>(.*?)</topic>'
        'sentence': '<sentence>(.*?)</sentence>'
    }
    extracted_entities = dict()
    for entity in regex.keys():
        extracted_entities[entity] = re.findall(r'' + regex[entity], data)
    return extracted_entities


def evaluate_tagging(pretagged, selftagged):
    correct = extract_sem_info(pretagged)
    made = extract_sem_info(selftagged)
    
    return ""


    

x = "Who: <speaker>Ramesh Bollapragada</speaker>, <stime>2:00</stime> G TO SCHEDULING STEEL PLANTS Time:<stime>1:00 PM</stime> Place:    <location>4623 WEAN HALL</location>"

y = extract_sem_info(x)
print(y)
print(y['stime'])
