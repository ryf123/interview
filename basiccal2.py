class Solution(object):
	def calculate(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		numstack = []
		operators = []
		l = len(s)
		i=0
		while i<l:
			if s[i].isdigit():
				start = i
				while i<l and s[i].isdigit():
					i+=1
				numstack.append(int(s[start:i]))
			elif s[i] in ["+","-","*","/"]:
				operators.append(s[i])
				i+=1
			else:
				i+=1
		# if there is n operator then there is n+1 nums
		for i,operator in enumerate(operators):
			if operator in ["*","/"]:
				num1,num2 = numstack[i],numstack[i+1]
				if operator == "*":
					numstack[i],numstack[i+1] = 0,num1*num2
				else:
					ret = abs(num1)/num2
					if num1 < 0:
						ret = -ret 
					numstack[i],numstack[i+1] = 0,ret
			elif operator== "-":
				numstack[i+1] = 0-numstack[i+1]
				# operators[i] = operators[i-1] if i-1 >=0 else "+"
		if len(numstack) == 0:
			return 0
		return sum(numstack)
		# total = numstack[0]
		# for i,operator in enumerate(operators):
		# 	if operator == "+":
		# 		total += numstack[i+1]
		# 	else:
		# 		total -= numstack[i+1]
		# return total





s = Solution()
st = ["14/3*2","13+2*2-3/2","1","1+1","3*3","1-2*2*2*2","0/2-2","42","1 + 1 * 2","100000000000/1/2/3/4/5/6/7/8/9/1/1/1/1/1/1/1/1/1/1/1/1/1"]
# for x in xrange(13):
# 	st +=st
# print st
for t in st:
	if s.calculate(t) != eval(t):
		print t,s.calculate(t),eval(t)
	# break