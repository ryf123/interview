class Solution(object):
	def minDistance(self, word1, word2):
		"""
		:type word1: str
		:type word2: str
		:rtype: int
		"""
		l1 = len(word1)
		l2 = len(word2)
		dp = [[0]*(l2+1) for x in xrange(l1+1)]
		for x in xrange(l2+1):
			dp[0][x] = x
		for x in xrange(l1+1):
			dp[x][0] = x
		for row in xrange(1,l1+1):
			for col in xrange(1,l2+1):
				if word1[row-1] == word2[col-1]:
					dp[row][col] = min(dp[row-1][col-1],dp[row-1][col]+1,dp[row][col-1]+1) 
				else:
					dp[row][col] = min(dp[row-1][col-1],dp[row-1][col],dp[row][col-1]) +1

		# print dp
		return dp[l1][l2] 
s = Solution()
tests = [["abc","adbef"],["a",""],["","b"],["aa","a"],["abc","aabcd"]] 
for t in tests:
	print s.minDistance(t[0],t[1])
