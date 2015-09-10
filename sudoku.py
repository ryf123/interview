class Solution:
	# @param {character[][]} board
	# @return {void} Do not return anything, modify board in-place instead.
	def solveSudoku(self, board):
		l = len(board)
		if l == 9:
			if len(board[0]) == 9:
				ret =  self.solve(board,0,0)
				return ret
		return False
	def solve(self,board,row,col):
		# print (row,col,board)
		if row == 9:
			return True
		if col == 8:
			row2 = row+1
			col2 = 0
		else:
			row2 = row
			col2 = col+1
		if board[row][col] != ".":
			if not self.valid(board,row,col):
				return False
			return self.solve(board,row2,col2)
		for i in range(1,10):
			board[row][col] = str(i)
			if self.valid(board,row,col) and self.solve(board,row2,col2):
				return True
		board[row][col] = "."
		return False

	def valid(self,board,row,col):
		# check row,
		val = board[row][col]
		for i in range(0,9):
			if  board[row][i] == val and i != col:
				return False
			if board[i][col] == val and i != row:
				return False
		row2 = row/3*3
		col2 = col/3*3
		for i in range(row2,row2+3):
			for j in range(col2,col2+3):
				if board[i][j] == val and (i!= row or j!=col):
					return False
		return True
s = Solution()
board = []
for row in ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]:
	board.append(list(row))
print board
print s.solveSudoku(board)
print board