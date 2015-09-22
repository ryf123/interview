# Definition for an interval.
class Interval(object):
	def __init__(self, s=0, e=0):
		self.start = s
		self.end = e

class Solution(object):
	def insert(self, intervals, newInterval):
		"""
		:type intervals: List[Interval]
		:type newInterval: Interval
		:rtype: List[Interval]
		"""
		start,end = newInterval.start,newInterval.end
		i = 0
		l = len(intervals)
		while i<l and intervals[i].start < start:
			i+=1
		if i-1>=0 and start>= intervals[i-1].start and start <= intervals[i-1].end:
			i=i-1
			start = intervals[i].start
		j = i
		while j<l and intervals[j].end <= end:
			j+=1
		if j <l and end >= intervals[j].start and end<= intervals[j].end:
			end = intervals[j].end
			j = j+1
		return intervals[:i] + [Interval(start,end)] + intervals[j:]
		

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
