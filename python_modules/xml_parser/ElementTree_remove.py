import xml.etree.ElementTree as ET
mytree = ET.parse('sample.xml')
myroot = mytree.getroot()
myroot[0].remove(myroot[0][0])
mytree.write('new4.xml')