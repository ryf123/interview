class Solution:
	# @param {integer} n
	# @return {string[][]}
	def solveNQueens(self, n):
		def solve(board,col,n):
			#print (board,col,n)
			if col >= n:
				return (True,board)
			for i in range(0,n):
				#print i
				if(self.isSafe(board,i,col,n)):
					board[i][col] = 1
					ret,myboard = solve(board,col+1,n)
					if ret : # if there is one solution,then continue with other solution						
						result.append(self.convertboard(myboard))
						#print result
						#print ret
					board[i][col] = 0
			return (False,result)
		board = [[0]*n for x in range(0,n)]
		#print board
		result = []
		ret,board = solve(board,0,n)		
		return result
	def convertboard(self,board):
		result = []
		for i in board:
			temp = ""
			for j in i:
				if j:
					temp+="Q"
				else:
					temp+="."
			result.append(temp)
		return result
	def isSafe(self,board,x,y,n):
		for i in range(0,y):
			if(board[x][i]):
				return False
		i = x
		j = y
		while(i>= 0 and j>=0):
			if board[i][j]:
				return False
			i-=1
			j-=1
		i = x
		j = y
		while(j>=0 and i <n):
			if board[i][j]:
				return False
			i+=1
			j-=1
		return True

s = Solution()
print s.solveNQueens(8)