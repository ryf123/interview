class Solution:
	# @param {integer} m
	# @param {integer} n
	# @return {integer}
	def uniquePathsWithObstacles(self, obstacleGrid):
		# DP return board[0][0] which is the sum of board[0][1] + baord[1][0]
		# initialize board
		m = len(obstacleGrid)
		if m == 0:
			return 0
		n = len(obstacleGrid[0])
		boardrow = [1]*n
		board = [boardrow[:] for x in range(0,m)]
		# initialize right most column
		# if last one is obstacle return 0
		if obstacleGrid[m-1][n-1]:
			return 0
		for  i in range(m-2,-1,-1):
			if obstacleGrid[i][n-1]:
				board[i][n-1] = 0
			else:
				board[i][n-1] = board[i+1][n-1] 
		# initialize last row
		for j in range(n-2,-1,-1):
			if obstacleGrid[m-1][j]:
				board[m-1][j] = 0
			else:
				board[m-1][j] = board[m-1][j+1]
		if m == 1 or n ==1:
			return board[0][0]
		# start from the right bottom
		#print board
		for i in range(m-2,-1,-1):
			for j in range(n-2,-1,-1):
				if obstacleGrid[i][j]:
					board[i][j] = 0
				else:
					board[i][j] = board[i+1][j] + board[i][j+1]
		return board[0][0]
s = Solution()
row = [0]*3
obstacle =[row[:] for x in [1,2,3]]
obstacle[1][1] = 1
obstacle = [[0,0],[1,1],[0,0]]
print s.uniquePathsWithObstacles(obstacle)