# -*- coding: utf-8 -*-  Non-ASCII character '\xe2'
# 实现一个mini parser, 输入是以下格式的string: ”[123,456,[788,799,833],[[]],10,[]]”
# 要求输出:  [123,456,[788,799,833],[[]],10,[]]	
class miniParser:
	def parse(self,s):
		l = len(s)
		stack,end = self.parse_stack(0,s,l)
		return stack[0]
	def parse_stack(self,start,s,l):
		stack = []
		substack = []
		i = start
		while i<=l:
			if i==l or s[i] == "," or s[i] == "]":
				if not substack:
					stack.append(s[start:i])
				else:
					stack.append(substack)
					substack = []
				if i==l or s[i] == "]":
					return stack,i
				start = i+1
			elif s[i] == "[":
				substack,i = self.parse_stack(i+1,s,l)
			i+=1
		return stack,i
mp = miniParser()
print mp.parse("123")
print mp.parse("[123,456,[788,799,833],[[]],10,[]]")




