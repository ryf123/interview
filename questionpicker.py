from pyquery import PyQuery
import re
import random
from urllib2 import *
class QuestionPicker:
	def __init__(self):
		self.questions = []
		self.readfile()
	def readfile(self):
		pattern = "^\d{1,3}\t(.*)\t\d{2}"
		with open("leetcode.txt","r") as f:
			for line in f:
				m = re.search(pattern,line)
				if m:
					self.questions.append(m.groups(1)[0])
	def generateRandom(self):
		index = int(random.uniform(0,len(self.questions)-1))
		self.getquestion(self.questions[index])
	def getquestion(self,url):
		url = url.replace(" ","-")
		print url
		urlstr = "https://leetcode.com/problems/"+url 
		url = urlopen(urlstr)
		lines = ""
		for line in url:
			lines +=line
		pq = PyQuery(lines)
		tag = pq("meta")
		desc = tag("meta").eq(2)
		print desc.attr("content")
qp = QuestionPicker()
print qp.generateRandom()
qp.getquestion("")