class Solution:
	# @param {integer} n
	# @return {string[][]}
	def solveNQueens(self, n):
		board = [["."]*n for x in xrange(n)]
		self.n = n
		sols = {}
		self.ret = []
		self.solve(board,0,sols)
		return self.ret
	def solve(self,board,row,sols):
		# print board
		if row ==self.n:
			result = []
			for b in board:
				result.append("".join(b))
			self.ret.append(result)
			return True
		for x in xrange(self.n):
			sols[row] = x
			board[row][x] = "Q"
			if self.isValid(board,sols,row,x):
				self.solve(board,row+1,sols)
			board[row][x] = "."
		del sols[row]
		return False
	def isValid(self,board,sols,row,col):
		# print row,col
		for key in sols:
			if sols[key] == col and key!= row:
				return False
		for x in range(-self.n,self.n):
			if row +x < self.n and row+x >=0:
				if col+x < self.n and col+x >=0:
					if board[row+x][col+x] == "Q" and x!=0:
						return False
				if col-x <self.n and col-x>=0:
					if board[row+x][col-x] == "Q" and x!=0	:
						return False
		return True
s = Solution()
ret =  s.solveNQueens(8)
print len(ret)