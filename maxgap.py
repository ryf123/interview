import sys
class Solution(object):
	def maximumGap(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		l = len(nums)
		
		if l==0:
			return 0
		minnum = min(nums)
		maxgap = max(nums) - minnum
		avggap = (maxgap) /(l)
		bucketsize = l+1
		buckets = [[] for x in xrange(bucketsize)]
		for num in nums:
			index = (num-minnum)/max(avggap,1)
			if len(buckets[index]) <2:
				buckets[index].append(num)
				buckets[index].sort()
			else:
				buckets[index][0]  = min(buckets[index][0],num)
				buckets[index][1] = max(buckets[index][1],num)
		# print buckets
		premax = None
		ret = 0
		for bucket in buckets:
			lb = len(bucket)
			if premax != None and lb:
				ret = max(bucket[0] - premax,ret)
			if lb ==2:
				premax = bucket[1]
			elif lb == 1:
				premax = bucket[0]
		return ret



sl = Solution()
nums = [1,2,9,8,10,90,100]
tests = [nums,[1,2],[1,1,1,1],[-1,-2,-10],[1],[sys.maxint]]
for t in tests:
	print sl.maximumGap(t)