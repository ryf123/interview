# Definition for an interval.
class Interval(object):
	def __init__(self, s=0, e=0):
		self.start = s
		self.end = e

class Solution(object):
	def insert(self, intervals,newInterval):
		"""
		:type intervals: List[Interval]
		:rtype: List[Interval]
		"""
		intervals.append(newInterval)
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
					# visited[i] = True
					# print i,intervals[i].start,end
					i+=1
					if i ==l:
						break
			ret.append(Interval(start,end))
		return ret
		

intervals = [Interval(1,2),Interval(2,6),Interval(8,10),Interval(15,18)]
# interval2 = [Interval(2,6),Interval(6,10)]
# interval3 = [Interval(1,100),Interval(1,2),Interval(1,10)]
s = Solution()
tests = [Interval(5,9),Interval(11,12),Interval(-1,0),Interval(18,21),Interval(5,7),Interval(7,9)]
for t in tests:
	ret = s.insert(intervals,t)
	for i in ret:
		print [i.start,i.end]
	print "==============="
