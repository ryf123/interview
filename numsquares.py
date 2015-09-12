import sys
class Solution(object):
	def numSquares(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		count = 0
		dp = [0]
		i = 0
		while len(dp) <=n:
			j = 1
			m  = len(dp)
			squares = sys.maxint
			while j*j <=m:
				squares = min(squares,(dp[m-j*j]+1))
				j+=1
			i+=1
			dp.append(squares)
		# print dp
		return dp[n]
s = Solution()
for t in range(2115,2116):
	print t,s.numSquares(t)
