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
		count = 0
		while not self.getquestion(self.questions[index]):
			count +=1 
			if count == 10:
				print "can't read any question, network issue?"
				break
	def getquestion(self,url):
		url = url.replace(" ","-")
		print url
		urlstr = "https://leetcode.com/problems/"+url
		try: 
			url = urlopen(urlstr)
			lines = ""
			for line in url:
				lines +=line
			pq = PyQuery(lines)
			tag = pq("meta")
			desc = tag("meta").eq(2)
			print desc.attr("content")
			tag = pq("span")
			difficulty = tag("span.total-submit")
			print difficulty.text()
		except Exception,e:
			print "Question is locked %s,no permission"%(str(url))
			return False
		return True
qp = QuestionPicker()
qp.generateRandom()
# qp.getquestion("Intersection-of-Two-Linked-Lists")