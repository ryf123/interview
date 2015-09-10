class Solution(object):
	def numIslands(self, grid):
		"""
		:type grid: List[List[str]]
		:rtype: int
		"""
		def mark(i,j,grid):
			grid[i][j] = "0"
			if i-1 >=0:
				if grid[i-1][j] == "1":
					mark(i-1,j,grid)
			if j-1>=0:
				if grid[i][j-1]== "1":
					mark(i,j-1,grid)
			if i+1 < self.row:
				if grid[i+1][j]== "1":
					mark(i+1,j,grid)
			if j+1 < self.column:
				if grid[i][j+1]== "1":
					mark(i,j+1,grid)

		self.row = len(grid)
		if not self.row:
			return 0
		self.column = len(grid[0])
		total = 0
		for i in xrange(self.row):
			for j in xrange(self.column):
				if grid[i][j] == "1":
					mark(i,j,grid)
					total+=1
		return total
s = Solution()
grid = ["11000","11000","00100","00011"]
grid = [list(x) for x in grid]
print grid
print s.numIslands(grid)