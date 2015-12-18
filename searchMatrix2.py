class Solution:
	# @param {integer[][]} matrix
	# @param {integer} target
	# @return {boolean}
	def searchMatrix(self, matrix, target):
		row = len(matrix)
		if row == 0:
			return False
		col = len(matrix[0])
		i,j = 0,col-1
		while i < row and j >=0:
			value = matrix[i][j]
			if value < target:
				i+=1
			elif value > target:
				j-=1
			else:
				return True 
		return False
s= Solution()
assert(s.searchMatrix([[1]],1))
assert(s.searchMatrix([[1]],2) == False)





