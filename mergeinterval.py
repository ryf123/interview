# Definition for an interval.
class Interval(object):
	def __init__(self, s=0, e=0):
		self.start = s
		self.end = e

class Solution(object):
	def merge(self, intervals):
		"""
		:type intervals: List[Interval]
		:rtype: List[Interval]
		"""
		intervals = sorted(intervals,key=lambda x:x.start)
		l = len(intervals)
		visited = [False] *l
		i = 0
		ret = []
		while i<l:
			if visited[i]:
				i+=1
				continue
			start,end = intervals[i].start,intervals[i].end
			i+=1
			if i<l:
				while(intervals[i].start <= end and i<l):
					if intervals[i].end > end:
						end = intervals[i].end
					visited[i] = True
					# print i,intervals[i].start,end
					i+=1
					if i ==l:
						break
			ret.append(Interval(start,end))
		return ret
s  = Solution()

intervals = [Interval(8,10),Interval(1,3),Interval(15,18),Interval(2,6)]
interval2 = [Interval(2,6),Interval(6,10)]
interval3 = [Interval(1,100),Interval(1,2),Interval(1,10)]
tests = [intervals,interval2,interval3]
for t in tests:
	ret = s.merge(t)
	for r in ret:
		print [r.start,r.end]
	print "==============="