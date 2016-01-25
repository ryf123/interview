# -*- coding: utf-8 -*-  Non-ASCII character '\xe2'
# csv parser
# 如果有逗号，转化成|
# 如果有引号，不考虑引号里逗号，把引号里的内容去引号整体打印。
# 如果有两重引号，只去掉一重引号。

# 例子
# aa, bb, “aa”,”aa,bb”, “aa””aa”””
# 输出
# aa|bb|aa|aa,bb|aa”aa”
class Solution:
	def parse(self,s):
		l = len(s)
		ret = ""
		i = 0
		string = ""
		quote = 0
		start = 0
		s = list(s)
		open_quote,close_quote = -1,-1
		while i<l:
			if (s[i] == "," and quote%2 == 0):
				s[i] = "|"
				close_quote = -1
				quote = 0
			elif s[i] == '"':
				if quote == 0:
					s[i] = ''
				else:
					if close_quote != -1:
						s[close_quote] = '"'
					close_quote = i
					s[close_quote] = ''
				quote+=1
			i +=1
		return "".join(s)
s = Solution()
string = r'aa,"""bb""","aa","aa,bb","aa""aa"""'
print s.parse(string) 


