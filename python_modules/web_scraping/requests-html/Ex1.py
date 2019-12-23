from requests_html import HTML, HTMLSession
import csv

csv_file = open('corey_scrape.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video'])

session = HTMLSession()
r = session.get('https://coreyms.com/')

articles = r.html.find('article')
# print(articles.html)

for article in articles:
	# print(article.html)
	headline = article.find('.entry-title-link', first=True).text
	print(headline)
	summary = article.find('.entry-content p', first=True).text
	print(summary)
	try:
		vid_id = article.find('figure', first=True).text
		vid_id = vid_id.split('/')[3]
		yt_link = f"https://www.youtube.com/watch?v={vid_id}"
		print(yt_link)
	except Exception as e:
		yt_link = None
	print()
	csv_writer.writerow([headline, summary, yt_link])

csv_file.close()