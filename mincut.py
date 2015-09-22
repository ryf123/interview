class Solution(object):
	def minCut(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		l =  len(s)
		if l ==0:
			return s
		dp = [[False]*l for x in range(0,l)]
		# maxlen = 0
		for i in range(l-1,-1,-1):
			for j in range(i,l):
				if (s[i] == s[j] and (j-i<=1 or dp[i+1][j-1])):
					dp[i][j] = True
		return dp[0][0]

s = Solution()
print s.minCut("aaaaba")