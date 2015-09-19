class Solution:
	# @param triangle, a list of lists of integers
	# @return an integer
	def minimumTotal(self, triangle):
		tcopy = [row[:] for row in triangle]
		m = len(triangle)
		if m ==0:
			return 0
		if m ==1:
			return triangle[0][0]
		for i in range(m-2,-1,-1):
			row = triangle[i]
			for j,t in enumerate(row):
				triangle[i][j] = min(triangle[i+1][j],triangle[i+1][j+1]) + triangle[i][j]
		return triangle[0][0]
s = Solution()
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
print s.minimumTotal(triangle)


