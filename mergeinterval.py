# Definition for an interval.
class Interval(object):
	def __init__(self, s=0, e=0):
		self.start = s
		self.end = e

class Solution(object):
	def merge(self, intervals):
		def compare(a,b):
			return -1 if a.start < b.start else 1 
		intervals = sorted(intervals,cmp=compare)
		prevstart,prevend = None,None
		ret = []
		for interval in intervals:
			start,end = interval.start,interval.end
			if prevend != None:
				if prevend >= start:
					start,end = prevstart,end
					previnterval = ret.pop()
					end = max(previnterval.end,end)
			ret.append(Interval(start,end))
			prevstart,prevend = start,end
		return ret
s = Solution()
intervals = [Interval(8,10),Interval(1,3),Interval(15,18),Interval(2,6)]
interval2 = [Interval(0,0),Interval(0,0),Interval(0,6)]
interval3 = [Interval(1,100),Interval(1,2),Interval(1,10)]
# [[0,0],[1,2],[5,5],[2,4],[3,3],[5,6],[5,6],[4,6],[0,0],[1,2],[0,2],[4,5]]
tests = [intervals,interval2,interval3]
for t in tests:
	ret = s.merge(t)
	for r in ret:
		print [r.start,r.end]
	print "==============="