class Solution(object):
	def addOperators(self, nums, target):
		"""
		:type nums: str
		:type target: int
		:rtype: List[str]
		"""
		self.target = target
		self.l = len(nums)
		divides = self.divide(0,nums)
		self.ret = []
		print len(divides)
		for divide in divides:
			# self.getoperator(len(divide))
			self.cal(divide,self.getoperator(len(divide)),target)
		return self.ret
	def getoperator(self,n):
		result = [["+"]]
		if n == 1:
			return result
		for x in xrange(n-1):
			tempresult = []
			for o in ["+","-","*"]:
				for r in result:
					tempresult.append(r+[o])
			result = tempresult
		return result
	# the num combination, target number and previous operator
	def cal(self,divide,operatorarray,target):
		for operators in operatorarray:
			stack = []
			for i,o in enumerate(operators):
				# tempret += o + divide[i]
				if o == "+":
					stack.append(int(divide[i]))
				elif o == "-":
					stack.append(-int(divide[i]))
				elif o=="*":
					# print [stack[-1],divide[i]]
					stack.append(stack.pop()*int(divide[i]))
			if sum(stack) == target:
				tempret = ""
				for i in xrange(len(operators)):
					tempret += operators[i]+divide[i]
				self.ret.append(tempret[1:])
		return	
	# first divide the digits
	def divide(self,start,nums):
		result = []
		if start == self.l:
			return []
		result.append([nums[start:]])
		for i in range(start,self.l):
			rets = self.divide(i+1,nums)
			for r in rets:
				result.append([nums[start:i+1]]+r)
		return result
s = Solution()
# print s.getoperator(3)
tests = [["123", 6],["232", 8],["00",0],["3456237490", 9191],["1000000009", 9]]
for t in tests:
	t = tests[3]
	r  = s.addOperators(t[0],t[1])
	print r
	break
	