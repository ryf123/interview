class Solution:
	# @param {integer[][]} matrix
	# @return {integer[]}
	def generateMatrix(self,n):
		def spiral(x,y,row,col,start):
			for j in range(y,y+col):
				self.matrix[x][j] = start
				start +=1
			if x+1 < x+row:
				for i in range(x+1,x+row):
					# print i,y+col-1
					self.matrix[i][y+col-1] = start
					start +=1
			if y+col-2 > y and row != 1:
				for j in range(y+col-2,y,-1):
					# print x+row-1,j
					self.matrix[x+row-1][j] = start
					start +=1
			if x+row-1 > x and col != 1:
				for i in range(x+row-1,x,-1):
					self.matrix[i][y] = start
					start +=1
			if row>2 and col>2:
				spiral(x+1,y+1,row-2,col-2,start)
		self.ret = []
		self.matrix = [[0]*n for x in xrange(n)]
		spiral(0,0,n,n,1)
		return self.matrix
s = Solution()
print s.generateMatrix(3)