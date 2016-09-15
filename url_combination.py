# -*- coding: utf-8 -*-  Non-ASCII character '\xe2'
#给一个string, app[1,2].corp[3,4].com要求返回：
#app1.corp3.com, app2.corp3.com, app1.corp4.com, app2.corp4.com.组合题变种
import re
def traverse(lists,lists_index,ret,path):
	if(lists_index == len(lists)):
		ret.append(list(path))
		return
	for i in xrange(len(lists[lists_index])):
		part = lists[lists_index][i]
		path.append(part)
		traverse(lists,lists_index+1,ret,path)
		path.pop()

def find(s):
	parts = s.split(".")
	lists = []
	for part in parts:
		m = re.search("\[([,\d]+)\]",part)
		if m:
			list = []
			options = m.group(1)
			for option in options.split(","):
				list.append(part.split("[")[0] + option) 
		else:
			list = [part]
		lists.append(list)
	ret = []
	traverse(lists,0,ret,[])
	print ret

s = "app[13,20].corp[3,4].com"
find(s)



