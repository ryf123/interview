class Solution(object):
	def calculateMinimumHP(self, dungeon):
		"""
		:type dungeon: List[List[int]]
		:rtype: int
		"""

		row = len(dungeon)
		if row == 0:
			return
		col = len(dungeon[0])
		hp = [[0]*col for x in xrange(row)]
		for x in range(row-1,-1,-1):
			for y in range(col-1,-1,-1):
				if x==row-1 and y==col-1:
					hp[x][y] = max(-dungeon[x][y]+1,1)
				elif x==row-1:
					if dungeon[x][y] <= 0:
						hp[x][y] = max(hp[x][y+1],1) - dungeon[x][y]
					else:
						hp[x][y] = 1 if dungeon[x][y] - hp[x][y+1] >0 else max(hp[x][y+1] - dungeon[x][y],1)
				elif y == col-1:
					if dungeon[x][y] <=0:
						hp[x][y] = max(hp[x+1][y],1) - dungeon[x][y]
					else:
						hp[x][y] = 1 if dungeon[x][y] - hp[x+1][y] >0 else max(hp[x+1][y] - dungeon[x][y],1)
				else:
					if dungeon[x][y] <=0:
						hp[x][y] = max(min(hp[x+1][y],hp[x][y+1]),1) - dungeon[x][y]
					else:
						minval =  min(hp[x+1][y],hp[x][y+1])
						hp[x][y] = 1 if dungeon[x][y] - minval >0 else max(minval - dungeon[x][y],1)
		# print hp
		return hp[0][0]
s = Solution()
dungeon = [[-2,-3,3],[-13,-10,1],[10,30,-5]]
# dungeon = [[2],[1]]
# dungeon = [[2,0,-1]]
print s.calculateMinimumHP(dungeon)