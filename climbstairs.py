class Solution(object):
	def climbStairs(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		if n<1:
			return 0
		if n ==1:
			return 1
		twostepback = 1
		onestepback = 1
		for i in range(2,n+1):
			temp = onestepback
			onestepback = onestepback + twostepback
			twostepback = temp
		return onestepback
s = Solution()
for i in xrange(10):
	print i,s.climbStairs(i)
