class Solution:
	# @param {integer[][]} matrix
	# @return {void} Do not return anything, modify matrix in-place instead.
	def rotate(self, matrix):
		l = len(matrix)
		copy = [ x[:] for x in matrix]
		for i in range(0,l):
			for j in range(0,l):
				matrix[i][j] = copy[l-j-1][i]
		return matrix
s = Solution()
print s.rotate([[1,2],[3,4]])