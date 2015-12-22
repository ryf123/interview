class Solution(object):
	def calculateMinimumHP(self, dungeon):
		"""
		:type dungeon: List[List[int]]
		:rtype: int
		"""
		if len(dungeon) == 0:
			return 0
		row,col = len(dungeon),len(dungeon[0])
		if col == 0:
			return 0
		hpmatrix = [[0] * col for x in xrange(row)]
		hpmatrix[row-1][col-1] = 1 if dungeon[row-1][col-1]>0 else 1+abs(dungeon[row-1][col-1])
		i = row-2
		while i>=0:
			hpmatrix[i][col-1] = max(hpmatrix[i+1][col-1]-dungeon[i][col-1],0) if dungeon[i][col-1] >0 else hpmatrix[i+1][col-1]-dungeon[i][col-1] + (1 if hpmatrix[i+1][col-1]==0 else 0)
			hpmatrix[i][col-1] = max(hpmatrix[i][col-1],1)
			i-=1
		j = col-2
		while j>=0:
			hpmatrix[row-1][j] = max(hpmatrix[row-1][j+1]-dungeon[row-1][j],0) if dungeon[row-1][j] >0 else hpmatrix[row-1][j+1]-dungeon[row-1][j] +  (1 if hpmatrix[row-1][j+1]==0 else 0)
			hpmatrix[row-1][j] = max(hpmatrix[row-1][j],1)
			j-=1
		i = row-2
		while i>=0:
			j = col-2
			while j>=0:
				hpmatrix[i][j] = min(max(hpmatrix[i+1][j]-dungeon[i][j],0) if dungeon[i][j] >0 else hpmatrix[i+1][j]-dungeon[i][j]+ (1 if hpmatrix[i+1][j]==0 else 0),max(hpmatrix[i][j+1]-dungeon[i][j],0) if dungeon[i][j] >0 else hpmatrix[i][j+1]-dungeon[i][j]+  (1 if hpmatrix[i][j+1]==0 else 0))
				hpmatrix[i][j] = max(hpmatrix[i][j],1)
				j-=1
			i-=1
		return hpmatrix[0][0]
dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
dungeon = [[1,-3,3],[0,-2,0],[-3,-3,-3]]
s = Solution()
print s.calculateMinimumHP(dungeon)	
