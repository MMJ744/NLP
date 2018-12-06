from anytree import Node, RenderTree

root_node = Node('root')
ids = dict()

computer_science = Node('computer_science', parent=root_node, ids=set())
ai = Node('AI', parent=computer_science)
functional = Node('Functional', parent=computer_science)
nlp = Node('NLP', parent=ai)
one = Node('hi', parent=root_node, ids=set())

for pre, fill, node in RenderTree(computer_science):
	print("%s%s" % (pre, node.name))


def print_tree(root):
	for pre, fill, leaf in RenderTree(root):
		print("%s%s" % (pre, leaf.name))


def build_tree(topics):
	for (topic, number) in topics:
		if topic in root_node.children:
			x = Node(topic, parent=root_node, ids=set())
			ids[topic].add(number)
		else:
			ids[topic] = set([number])

def get_topic_ids(topic):
	if topic in root_node.children:




print(root_node.children)
build_tree([("a",2),("b",1),("c",3),("a",4),("c",5)])
print(root_node.children)
print(ids)