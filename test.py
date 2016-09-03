from bs4 import BeautifulSoup
from urllib2 import urlopen
import time
import pdb

BASE_URL = "http://www.codeproject.com/script/Answers/List.aspx?pgnum="
QUESTIONS_BASE_URL = "http://www.codeproject.com"

def get_question_urls(section_url):
	lst_urls = []
	for i in xrange(1, 10):
		try: 
			time.sleep(5)
			html = urlopen(BASE_URL + str(i)  + section_url)
			soup = BeautifulSoup(html, "lxml")
			something = soup.find_all("h3", "title")
			for item in something:
				for inner_item in item:
					try:
						yield inner_item['href']
					except:
						pass
		except Exception as e:
			print(e)


with open("data.txt", "w") as f:
	for url in get_question_urls(""):
		f.write(url + "\n")
	
