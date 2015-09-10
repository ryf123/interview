class Solution(object):
	def calculate(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		self.l = len(s)
		i = 0
		digitstack = []
		operatorstack = []
		while i<self.l:
			# print i,digitstack,operatorstack
			if s[i] == " ":
				i+=1
			elif s[i].isdigit():
				start = i
				while s[i].isdigit():
					if i+1 < self.l:
						i+=1
					else:
						i+=1
						break
				digit = s[start:i]
				digitstack.append(digit)
			# if s[i] is operator
			else:
				operator = s[i]
				i+=1
				if operator == "+" or operator == "-":
					operatorstack.append(operator)
				else:
					digit1 = int(digitstack.pop())
					i,digit2 = self.subcal(s,i,digit1,operator)
					digitstack.append(int(digit2))
						# print digitstack
		# print digitstack,operatorstack
		if len(digitstack) == 0:
			return 0
		total = int(digitstack.pop(0))
		while len(digitstack):
			o = operatorstack.pop(0)
			d = digitstack.pop(0)
			if o == "-":
				total -= int(d)
			else:
				total += int(d)
		return total

	def subcal(self,s,start,digit1,prevoperator):
		# print digit1,prevoperator
		i = start
		while(i<self.l):
			if s[i] == " ":
				i +=1
			elif s[i].isdigit():
				newstart = i
				while s[i].isdigit():
					if i+1 < self.l:
						i+=1
					else:
						i+=1
						break
				digit2 = int(s[newstart:i])
				if prevoperator == "*":
						ret = int(digit1)*int(digit2)
				else:
					ret = int(digit1)/int(digit2)
			else:
				operator = s[i]
				i+=1
				if operator == "+" or operator == "-":
					return i-1,ret
				else:
					return  self.subcal(s,i,ret,operator)
		return self.l,ret
s = Solution()
st = ["14/3*2","13+2*2-3/2","1","1+1","3*3","1-2*2*2*2","0/2-2","42","1 + 1 * 2","100000000000/1/2/3/4/5/6/7/8/9/1/1/1/1/1/1/1/1/1/1/1/1/1"]
# for x in xrange(13):
# 	st +=st
# print st
for t in st:
	if s.calculate(t) != eval(t):
		print t,s.calculate(t),eval(t)
	# break