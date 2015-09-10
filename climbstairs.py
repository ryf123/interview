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
		dp = (n+1)*[0]
		dp[0] = 1
		dp[1] = 1

		for i in range(2,n+1):
			dp[i] = dp[i-1]+dp[i-2]
		return dp[n]
s = Solution()
for i in xrange(10):
	print i,s.climbStairs(i)
