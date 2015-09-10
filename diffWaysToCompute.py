class Solution(object):
	def diffWaysToCompute(self, input):
		"""
		:type input: str
		:rtype: List[int]
		"""
		def calculate(start,end):
			# print start,end
			ret = []
			l = end-start
			if l == 1:
				# print start
				return [self.digits[start]]
			for i,digit in enumerate(self.digits[start:end]):
				if start+i == end-1:
					break
				# print i,start,end
				operator = self.operator[start+i]
				first = calculate(start,start+i+1)
				second = calculate(start+i+1,end)
				# print first,second
				for f in first:
					for s in second:
						if operator == "*":
							result = f*s
						elif operator == "+":
							result = f+s
						elif operator == "-":
							result = f-s
						ret.append(result)
			# print ret
			return ret
				# self.ret.append(result)
		self.digits,self.operator = self.processinput(input)
		# print self.digits,self.operator
		return calculate(0,len(self.digits))
	def processinput(self,input):
		l  = len(input)
		i = 0
		digits = []
		operator = []
		while i< l:
			if input[i].isdigit():
				start = i
				i +=1
				while i < l:
					if not input[i].isdigit():
						break
					i+=1
				digits.append(int(input[start:i]))
			else:
				operator.append(input[i])
				i+=1
		return digits,operator

s = Solution()
inputs = ["2*3-4*5","2*2*2","2-1-1","1"]
for i in inputs:
	print s.diffWaysToCompute(i)
