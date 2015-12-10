# from pyquery import PyQuery
import re
import random
import urllib2
from BeautifulSoup import BeautifulSoup

class QuestionPicker:
	def __init__(self):
		self.questions = {}
		# self.readfile()
	def readwebpage(self):
		lc_url = "https://leetcode.com/problemset/algorithms/"
		r = urllib2.urlopen(lc_url)
		soup = BeautifulSoup(r.read())
		for tr in soup('table')[1].tbody('tr'):
			if len(tr('td')) ==5:
				if not tr.i:
					prefix = "/problems/"
					name = tr.a["href"][len(prefix):-1]
					self.questions[name] = [tr('td')[1].text,tr('td')[3].text,tr('td')[4].text]
			else:
				print len(tr.td)
	def getquestionbfsoup(self,name):
		urlstr = "https://leetcode.com/problems/"+name
		r = urllib2.urlopen(urlstr)
		soup = BeautifulSoup(r.read())
		if len(soup("meta"))>=3:
			print soup("meta")[2]["content"].encode('utf-8').strip()
	def readfile(self):
		pattern = "^\d{1,3}\t(.*)\t\d{2}"
		with open("leetcode.txt","r") as f:
			for line in f:
				m = re.search(pattern,line)
				if m:
					self.questions.append(m.groups(1)[0])
	def generateRandom(self):
		print random.randint(1,255)
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
qp.readwebpage()
for key in qp.questions:
	print key,qp.questions[key]
	qp.getquestionbfsoup(key)
# qp.getquestion("Intersection-of-Two-Linked-Lists")