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


def get_related_data_to_question(ques_url):
	html = urlopen(QUESTIONS_BASE_URL + ques_url)
	soup = BeautifulSoup(html, "lxml")
	question_desc = soup.find("div", "header")
	user = soup.find("div", "member-rep-container").a.text
	profile_url = soup.find("div", "member-rep-container").a["href"]
	rating = soup.find("div", "member-rep-container").span.text
	tag0 = soup.find_all("span", "t")[0].text
	answer = soup.find("div", "answer-row answer first").find("div", "text").text
	#user = soup.find("a", id="ct100_ct100_MC_AMC_QuestionAuthorRepInfo_MemberName")
	print(answer)

#for url in get_question_urls(""):
#	get_related_data_to_question(url)
get_related_data_to_question("/Questions/1121991/How-can-I-calculate-time-interval-between-date-hou")
	
