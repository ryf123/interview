class Solution:
	# @param {integer[][]} matrix
	# @return {integer[]}
	def spiralOrder(self, matrix):
		def spiral(x,y,row,col):
			for j in range(y,y+col):
				self.ret.append(self.matrix[x][j])
			if x+1 < x+row:
				for i in range(x+1,x+row):
					# print i,y+col-1
					self.ret.append(self.matrix[i][y+col-1])
			if y+col-2 > y and row != 1:
				for j in range(y+col-2,y,-1):
					# print x+row-1,j
					self.ret.append(self.matrix[x+row-1][j])
			if x+row-1 > x and col != 1:
				for i in range(x+row-1,x,-1):
					# print i,y
					self.ret.append(self.matrix[i][y])
			if row>2 and col>2:
				# print x,y,row,col
				spiral(x+1,y+1,row-2,col-2)
		self.ret = []
		self.matrix = matrix
		m = len(matrix)
		if m == 0:
			return []
		n = len(matrix[0])
		spiral(0,0,m,n)
		return self.ret
s = Solution()
matrix = []
for x in xrange(40):
	temp = []
	for y in xrange(3):
		temp.append(y*10)
	matrix.append(temp) 
# matrix = [matrix1,matrix2,matrix3,matrix4]
for m in matrix:
	print m
ret  =  s.spiralOrder(matrix)
print ret
print len(ret)