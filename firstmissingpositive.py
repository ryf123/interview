class Solution(object):
	def firstMissingPositive(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		nums.append(0)
		m = max(nums)+1
		bucket = [0]*m
		for num in nums:
			if num > 0:
				bucket[num] = num
		for i in range(1,m):
			if bucket[i] != i:
				return i
		return m
s = Solution()
print s.firstMissingPositive([-1,-2,-3])