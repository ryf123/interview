class Solution(object):
	def isHappy(self, n):
		"""
		:type n: int
		:rtype: bool
		"""
		self.d = {}
		return self.breaknum(n)
	def breaknum(self,n):
		self.d[n] = True
		base = 10
		total = 0
		while(n):
			num = n%10
			total += num * num
			n = n/10
		if total == 1:
			return True
		else:
			if total in self.d:
				return False
			else:
				return self.breaknum(total)
s = Solution()
tests = [19,2,5,10,68,100,1,11,0]
for t in tests:
	print t,s.isHappy(t)
