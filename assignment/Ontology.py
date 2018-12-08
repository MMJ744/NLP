import anytree
from anytree import Node, RenderTree
from nltk.corpus import wordnet
import re

root_node = Node('root')
ids = dict()
nodes = dict()
nodes['misc'] = Node('misc', parent=root_node)  # Added the misc category in case a category cant be assigned
ids['misc'] = set()


def print_tree(root=root_node):
	if root in nodes.keys(): root = nodes[root]
	for pre, fill, leaf in RenderTree(root):
		print("%s%s" % (pre, leaf.name))


def getRelevant(topic):
	if topic in nodes.keys():
		main = nodes[topic]
		relevant = ids[topic]
		children = main.descendants
		for node in children:
			relevant = relevant.union(ids[node.name])
		return relevant
	else:
		print("Error topic not in tree")
		return []


def in_tree(name):
	y = anytree.search.find_by_attr(root_node, name='name', value=name)
	if (y):
		return True
	return False


def build_tree(groups, number):
	c = 0
	parent_node = ''
	for part in groups:
		if part != '':
			if c == 0:
				if in_tree(part):
					ids[part].add(number)
				else:
					ids[part] = set([number])
					nodes[part] = Node(part, parent=root_node)
				parent_node = part
				c = c + 1
			else:
				if in_tree(part):
					ids[part].add(number)
				else:
					ids[part] = set([number])
					nodes[part] = Node(part, parent=nodes[parent_node])
				parent_node = part


def get_topic(email, number):
	p = '(?:Type:\s*)(.*)'
	topic = set(re.findall(p, email)).pop()
	m = re.match('([^\.]*)\.?([^\.]*)\.?([^\.]*)\.?([^\.]*)\.?([^\.]*)\.?', topic)
	groups = [x for x in m.groups() if x]
	if groups[0] == 'cmu':
		groups.remove('cmu')
		build_tree(groups, number)
	else:
		topic = re.sub('\sSeminar', '', topic)
		print(topic)
		parent = ''
		syns = wordnet.synsets(topic)
		if len(syns) == 0:
			parent = 'misc'
		else:
			for syn in syns:
				deff = syn.definition()
				print(deff)
