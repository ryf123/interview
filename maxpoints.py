
# Definition for a point.
class Point(object):
	def __init__(self, a=0, b=0):
		self.x = a
		self.y = b
from collections import Counter
class Solution(object):
	def maxPoints(self, points):
		"""
		:type points: List[Point]
		:rtype: int
		"""
		maxpoints = 0
		i,l = 0,len(points)
		if l ==0:
			return 0
		if l == 1:
			return 1 
		for i in xrange(l-1):
			x1,y1 = points[i].x,points[i].y
			duplicate = 0
			cnt = Counter()
			for j in range(i+1,l):
				x2,y2 = points[j].x,points[j].y 
				if x1 == x2 and y1==y2:
					duplicate+=1
					continue
				elif y1 == y2:
					k = "inf"
				else:
					k = float(x1-x2)/(y1-y2)
				cnt[k] +=1
				# print k,[x1,y1],[x2,y2]
			# print duplicate,maxpoints,cnt
			for key in cnt:
				maxpoints = max(maxpoints,cnt[key]+duplicate)
			if len(cnt) == 0 and duplicate != 0:
				maxpoints = max(maxpoints,duplicate) 
		return maxpoints+1
p1 = Point(2,2)
p2 = Point(3,3)
p3 = Point(1,1)
points = []
test = [[-4,-4],[-8,-582],[-3,3],[-9,-651],[9,591]]
for p in test:
	points.append(Point(p[0],p[1]))
s = Solution()
# points = [p1,p2,p3]
print s.maxPoints(points)
