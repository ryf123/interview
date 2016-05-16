class Solution(object):
	def isSelfCrossing(self, x):
		"""
		:type x: List[int]
		:rtype: bool
		"""
		pos = [0,0]
		p = 0
		directions = [[0,1],[-1,0],[0,-1],[1,0]]
		vert = []
		horz = []
		for stride in x:
			index = p%4
			move = [stride * directions[index][0],stride * directions[index][1]]
			dest = [pos[0] + move[0], pos[1] + move[1]]
			if p%2 == 0: #vertical line
				x = pos[0]
				y1,y2 = pos[1],dest[1]
				vert.append([x,y1,y2])
				for h in horz[:-1]:
					[y,x1,x2] = h
					print [x,y1,y2],h,p,horz
					if x>= min(x1,x2) and x<=max(x1,x2) and y>= min(y1,y2) and y<= max(y2,y1):
						return True
			else: #horizontal line
				x1,x2 = pos[0],dest[1]
				y = pos[1]
				horz.append([y,x1,x2])
				for v in vert[:-1]:
					[x,y1,y2] = v

					if x>= min(x1,x2) and x<=max(x1,x2) and y>= min(y1,y2) and y<= max(y2,y1):
						return True 
			pos = dest
			p += 1
		return False
		
s = Solution()
print s.isSelfCrossing([1,1,2,1,1])