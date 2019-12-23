from requests_html import HTML, HTMLSession

session = HTMLSession()
r = session.get('https://coreyms.com/')

for link in r.html.links:
	print(link)

#absolute links
# for link in r.html.absolute_links:
# 	print(link)