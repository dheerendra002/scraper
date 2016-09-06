import MySQLdb
import time
import pdb

def insert_data(question_id, user="", profile_url="", rating="", answer="", source_website="", tags="", category="", correct_answer=""):
	sql_query = "INSERT INTO question_answer(question_short, user, profile_url, rating, answer, source_website, tags, category, \
	 correct_answer) VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s') " \
% (question_short, user, profile_url, rating, answer, source_website, tags, category, correct_answer)
	db = MySQLdb.connect("localhost", "root", "root", "scrape")
	cursor = db.cursor()
	try:
		cursor.execute(sql_query)
		db.commit()
		print("inserted")
	except Exception as e:
		print(e)
		db.rollback()
