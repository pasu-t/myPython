import xml.etree.ElementTree as ET
mytree = ET.parse('sample.xml')
myroot = mytree.getroot()
print(myroot)
print(myroot.tag)
print(myroot[0].tag)
print(myroot[0].attrib)
for x in myroot[0]:
	print(x.tag, x.attrib)
for x in myroot[0]:
	print (x.text)
for x in myroot.findall('food'):
	item = x.find('item').text
	price = x.find('price').text
	print(item,price)
for x in myroot.iter('description'):
	a = str(x.text) + " description has been added"
	x.text = a
	x.set('updated', 'yes')
mytree.write('new.xml')