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
		ret = []
		i,l = 0,len(intervals)
		if l == 0:
			return ret
		intervals.sort(key=lambda x:x.start)
		while i<l:
			interval = intervals[i]
			# print interval.start,interval.end
			start,end  =interval.start,interval.end
			while i+1 <l and intervals[i+1].start <= end:
				i+=1
				end = max(intervals[i].end,end)
				# print end,i+1,intervals[i].end
			ret.append(Interval(start,end))
			i+=1
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