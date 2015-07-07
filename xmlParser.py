__author__ = 'sdlee'

from xml.etree.ElementTree import parse
tree = parse("note.xml")
note = tree.getroot()

print "Note : ", note

print note.get("date")
print note.get("foo", "default")
print note.keys()
print note.items()

from_tag = note.find("from")
from_tags = note.findall("from")
from_text = note.findtext("from")



print "from_tag =", from_tag
print "from_tags =", from_tags
print "from_tag text =", from_text


childs_iterator = note.getiterator()
childs_children = note.getchildren()
print "Childs_iterator : ", childs_iterator
print "Childs_children : ", childs_children

childs_iterator = note.getiterator("from")
print "Childs_iterator of from: ", childs_iterator

# not support follow:
# childs_children = note.getchildren("from")
# print "Childs_children of from: ", childs_children