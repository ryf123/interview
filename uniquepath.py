class Solution:
	# @param {integer} m
	# @param {integer} n
	# @return {integer}
	def uniquePathsWithObstacles(self, obstacleGrid):
		m = len(obstacleGrid)
		if m == 0:
			return 0
		n = len(obstacleGrid[0])
		boardrow = [1]*n
		board = [[0] * (n+1) for x in range(0,m+1)]
		for i in xrange(1,m+1):
			for j in xrange(1,n+1):
				if i == 1 and j == 1 and obstacleGrid[0][0] == 0:
					board[i][j]  = 1
				else:
					if obstacleGrid[i-1][j-1] == 1:
						board[i][j] = 0
					else:
						board[i][j] = board[i-1][j] + board[i][j-1]
		return board[m][n]
		
s = Solution()
row = [0]*3
obstacle =[row[:] for x in [1,2,3]]
# obstacle[1][1] = 1
# obstacle = [[0,0],[1,1],[0,0]]
print s.uniquePathsWithObstacles(obstacle)