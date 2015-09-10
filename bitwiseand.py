class Solution(object):
	def rangeBitwiseAnd(self, m, n):
		"""
		:type m: int
		:type n: int
		:rtype: int
		"""
		p = 0
		while(m!=n):
			m>>=1
			n>>=1
			p+=1
		return n<<p
s  = Solution()
print s.rangeBitwiseAnd(90,100)