class Solution:
	# @param {integer[][]} matrix
	# @return {integer[]}
	def spiralOrder(self, matrix):
		def spiral(row,col):
			left,right,top,bottom = 0,col,0,row
			while left<=right and top<=bottom:
				i = left
				while i<=right:
					self.ret.append(self.matrix[top][i])
					i+=1
				top +=1
				i = top
				while i<=bottom:
					self.ret.append(self.matrix[i][right])
					i +=1
				right -=1
				i = right
				while i>=left and top<=bottom:
					self.ret.append(self.matrix[bottom][i])
					i -=1
				bottom -=1
				i = bottom
				while i>=top and left<=right:
					self.ret.append(self.matrix[i][left])
					i-=1
				left +=1
		self.ret = []
		self.matrix = matrix
		m = len(matrix)
		if m == 0:
			return []
		n = len(matrix[0])
		spiral(m-1,n-1)
		return self.ret
s = Solution()
matrix = []
count = 0
for x in xrange(3):
	temp = []
	for y in xrange(3):
		temp.append(count)
		count+=1
	matrix.append(temp) 
print matrix
print s.spiralOrder(matrix)
if __name__ == '__main__':
	main()
# matrix = [matrix1,matrix2,matrix3,matrix4]
# for m in matrix:
# 	print m
# ret  =  s.spiralOrder(matrix)
# print ret
# print len(ret)