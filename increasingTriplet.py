class Solution(object):
	def increasingTriplet(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		l = len(nums)
		if l < 3:
			return False
		less = [0] * l
		great = [0] * l
		minimum = nums[0]
		maximum = nums[-1]
		i = 0
		while i < l:
			minimum = min(nums[i],minimum)
			less[i] = minimum
			i += 1
		i = l - 1
		while i > 0:
			maximum = max(nums[i],maximum)
			great[i] = maximum
			i -= 1
		i = 0
		while i < l:
			if nums[i] > less[i] and nums[i] < great[i]:
				return True
			i += 1
		return False
s = Solution()
nums = [1,2,-1,-2,3]
print s.increasingTriplet(nums)