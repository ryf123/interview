class Solution(object):
	def maximalSquare(self, matrix):
		"""
		:type matrix: List[List[str]]
		:rtype: int
		"""
		max = 0
		row = len(matrix)
		if row == 0:
			return 0
		column = len(matrix[0])
		dp = [[0]*(column+1) for x in xrange(row+1)]
		for i in range(1,row+1):
			for j in range(1,column+1):
				if int(matrix[i-1][j-1]):
					dp[i][j] = min([dp[i-1][j-1],dp[i-1][j],dp[i][j-1]])+1
					max = dp[i][j] if dp[i][j] > max else max
		return max*max
s = Solution()
matrix = [[0]]
print s.maximalSquare(matrix)