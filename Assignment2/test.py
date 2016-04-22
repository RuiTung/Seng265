import libxml2
import sys

# parse the XML file in argv[1] and load it into memory
parse_tree = libxml2.parseFile(sys.argv[1])

# create a context for tree traversal
context = parse_tree.xpathNewContext()

# get the root of the tree
root = parse_tree.getRootElement()

# iterate over the children of root
child = root.children
while child is not None:
	if child.name == 'text':
		print 'text'

	if child.name == 'x':
		print 'x:', child.content

	if child.name == 'y':
		print 'y:', child.content

	child = child.next
