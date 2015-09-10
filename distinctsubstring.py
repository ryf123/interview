class Solution(object):
	def numDistinct(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: int
		"""
		row = len(t)
		col = len(s)
		dp = [[0]*(col+1) for x in xrange(row+1)]
		for i in xrange(col+1):
			dp[0][i] = 1
		for i in xrange(row):
			for j in xrange(col):
				dp[i+1][j+1] = dp[i+1][j] + (dp[i][j] if s[j] == t[i] else 0)
		return dp[row][col]
s  = Solution()
print s.numDistinct("rabbbitazdsd","rabbit")