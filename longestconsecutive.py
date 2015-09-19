class Solution(object):
	def longestConsecutive(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		l = len(nums)
		if l == 0:
			return 0
		maxnum,minnum = max(nums),min(nums)

		gap = (maxnum - minnum)/l
		buckets = [[] for x in xrange(l+1)]
		for num in nums:
			index = num/max(gap,1)
			buckets[index].append(num)
		print buckets
		newnums = []
		for bucket in buckets:
			bucket.sort()
			newnums += bucket
		# print newnums
		for i,num in enumerate(newnums):
			# print i,num,nums[i-1]
			if i==0:
				maxlen,con = 1,1
			else:
				if num-newnums[i-1] ==1:
					con +=1
					maxlen = max(con,maxlen)
				else:
					con =1
		return maxlen
s = Solution()
print s.longestConsecutive([0,-1])






