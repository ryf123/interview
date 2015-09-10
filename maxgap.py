class Solution(object):
	def maximumGap(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		l = len(nums)
		if l<2:
			return 0
		maxnum = max(nums)
		minnum = min(nums)
		bucketsize = max(1,(maxnum - minnum)/l)
		bucketcount = (maxnum-minnum)/(bucketsize) +1
		buckets = [[] for x in xrange(bucketcount)]
		maxgap = 0
		for num in nums:
			div = (num-minnum)/bucketsize
			buckets[div].append(num)
		# print buckets
		for i,bucket in enumerate(buckets):
			if not bucket:
				continue
			bucket.sort()
			if i==0:
				prevmax = bucket[-1]
				continue
			else:
				currentmin = bucket[0]
				if currentmin - prevmax > maxgap:
					maxgap = currentmin - prevmax
				prevmax = bucket[-1]
		return maxgap

sl = Solution()
nums = [1,9,8]
print sl.maximumGap(nums)