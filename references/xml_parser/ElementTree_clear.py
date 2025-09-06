import xml.etree.ElementTree as ET
mytree = ET.parse('sample.xml')
myroot = mytree.getroot()
myroot[0].clear()
mytree.write('new5.xml')