class Solution(object):
	def longestConsecutive(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		l = len(nums)
		d = {}
		maxlen = 0
		for num in nums:
			d[num] =True
		for key in d:
			if d[key]:
				j = 1
				currentlen = 1
				while (key+j) in d:
					currentlen +=1
					d[key+j] = False
					j+=1
					# print j
				k=1
				while (key-k) in d:
					currentlen +=1
					d[key-k] = False
					k+=1
					# print k
				maxlen = max(currentlen,maxlen)
		return maxlen


s = Solution()
print s.longestConsecutive([100, 4, 200, 1, 3, 2,0,-1])
