import xml.etree.ElementTree as ET
mytree = ET.parse('sample.xml')
myroot = mytree.getroot()
myroot[0][0].attrib.pop('name')
mytree.write('new3.xml')