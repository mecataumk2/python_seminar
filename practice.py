__author__ = 'sdlee'

import xml.etree.ElementTree as ET

tree = ET.parse("0031c45f7670b050a02624fdccb53537")
root = tree.getroot()
print list(root)

