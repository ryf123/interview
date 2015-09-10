class Solution(object):
	def setZeroes(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: void Do not return anything, modify matrix in-place instead.
		"""
		drow = {}
		dcol = {}
		row = len(matrix)
		if not row:
			return
		col = len(matrix[0])
		for i in xrange(row):
			for j in xrange(col):
				if not matrix[i][j]:
					drow[i],dcol[j] = True,True
		# print drow,dcol
		for i in drow:
			for x in xrange(col):
				matrix[i][x] = 0 
		for j in dcol:
			for x in xrange(row):
				matrix[x][j] = 0 
s = Solution()
matrix = [[0,0]]
s.setZeroes(matrix)
print matrix