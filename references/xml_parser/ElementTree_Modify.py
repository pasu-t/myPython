import xml.etree.ElementTree as ET
mytree = ET.parse('sample.xml')
myroot = mytree.getroot()
print(dir(ET))
ET.SubElement(myroot[0], 'speciality')
for x in myroot.iter('speciality'):
	b = "South Indian special"
	x.text = b
mytree.write('new2.xml')