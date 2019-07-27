from xml.dom import minidom
mytree = minidom.parse('sample.xml')
tagname = mytree.getElementsByTagName('item')[0]
tagname2 = mytree.getElementsByTagName('item')
print(tagname)
print(tagname.attributes['name'].value)
print(tagname.firstChild.data)
print(tagname2[1].firstChild.data)
print(len(tagname2))
for x in tagname2:
	print(x.firstChild.data)