class Solution:
	# @param {integer} m
	# @param {integer} n
	# @return {integer}
	def minPathSum(self, grid):
		# DP return board[0][0] which is the sum of board[0][1] + baord[1][0]
		# initialize board
		m = len(grid)
		if m == 0:
			return 0
		n = len(grid[0])
		boardrow = [0]*n
		board = [boardrow[:] for x in range(0,m)]
		board[m-1][n-1] = grid[m-1][n-1]
		# initialize right most column
		# if last one is obstacle return 0
		for  i in range(m-2,-1,-1):
			board[i][n-1] = grid[i][n-1] + board[i+1][n-1] 
		# initialize last row
		for j in range(n-2,-1,-1):
			board[m-1][j] = grid[m-1][j] + board[m-1][j+1]
		if m == 1 or n ==1:
			return board[0][0]
		# start from the right bottom
		#print board
		for i in range(m-2,-1,-1):
			for j in range(n-2,-1,-1):
				board[i][j] = grid[i][j]+ min(board[i+1][j],board[i][j+1])
		# print board
		return board[0][0]
s = Solution()
gridrow = [0]*3
grid = [gridrow[:] for x in [1,2]]
print grid
print s.minPathSum(grid)