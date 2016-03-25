class Solution(object):
	def longestIncreasingPath(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: int
		"""
		longest = 0
		m = len(matrix)
		if m > 0 :
			n = len(matrix[0])
		else:
			return 0
		self.length = [[-1]*n for i in xrange(m)]
		self.matrix = matrix
		self.m,self.n = m,n
		for row in xrange(m):
			for col in xrange(n):
				if self.length[row][col] == -1:
					longest = max(longest,self.dfs(row,col))
		return longest 
	def dfs(self,row,col):
		if self.length[row][col] != -1:
			return self.length[row][col]
		longest  = 0
		moves = [[0,1],[0,-1],[1,0],[-1,0]]
		for move in moves:
			_row,_col = row + move[0],col + move[1]
			if _row >= 0 and _row < self.m and _col >= 0 and _col < self.n and self.matrix[_row][_col] > self.matrix[row][col]:

				longest = max(self.dfs(_row,_col),longest)
		longest += 1
		self.length[row][col] = longest
		return longest
s = Solution()
matrix = [[3,4,5],[3,2,6],[2,2,1]]
print s.longestIncreasingPath(matrix)

		