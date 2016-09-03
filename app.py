from bs4 import BeautifulSoup
from urllib2 import urlopen
import time
import pdb
from mysql_helper import insert_data
import re

BASE_URL = "http://www.codeproject.com/script/Answers/List.aspx?pgnum="
QUESTIONS_BASE_URL = "http://www.codeproject.com"

def get_question_urls(section_url):
	lst_urls = []
	for i in xrange(1, 15000):
		try: 
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

def get_all_tags(soup):
	tags = soup.find_all("span", "t")
	tag_output = ""
	for tag in tags:
		tag_output += tag.text + ","

	return tag_output
		

def get_related_data_to_question(ques_url):
	html = urlopen(QUESTIONS_BASE_URL + ques_url)
	soup = BeautifulSoup(html, "lxml")
	question_desc = soup.find("div", "header").text
	user = soup.find("div", "member-rep-container").a.text
	profile_url = soup.find("div", "member-rep-container").a["href"]
	profile_url += BASE_URL
	rating = soup.find("div", "member-rep-container").span.text
	tags = get_all_tags(soup)
	category = ""
	answer = soup.find("div", "answer-row answer first").find("div", "text").text
	#user = soup.find("a", id="ct100_ct100_MC_AMC_QuestionAuthorRepInfo_MemberName")
	insert_data(question_id=question_desc, user=user, rating=rating, tags=tags, profile_url=profile_url, source_website=BASE_URL, answer=re.escape(answer), correct_answer=re.escape(answer), category=category)

for url in get_question_urls(""):
	try: 
		get_related_data_to_question(url)
	except Exception as e:
		print(e)
	
