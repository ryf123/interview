class Solution(object):
	def calculate(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		operator = ["+"]
		stack = []
		prev = "+"
		l  = len(s)
		total,i = 0,0
		while(i<l):
			# print operator
			o = s[i]
			if o == "+" or o =="-":
				if stack:
					if stack[-1] == "-":
						prev  = "+" if o =="-" else "-"
						operator.append(prev)
					else:
						operator.append(o)
						prev =o
				else:
					operator.append(o)
					prev = o
			elif o == "(":
				stack.append(prev)
			elif o == ")":
				stack.pop()
			elif o.isdigit():
				start = i
				while( i<l and s[i].isdigit()):
					i+=1
				if operator.pop() == "+":
					total+= int(s[start:i])
				else:
					total -= int(s[start:i])
				continue
			i+=1
		return total



s = Solution()
print s.calculate("(3-(2-(5-(9-(4)))))")