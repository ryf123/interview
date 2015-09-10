class Solution(object):
	def rotate(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		l = len(nums)
		k = k%l
		numscopy = list(nums)
		numscopy = numscopy[l-k:] + numscopy[:l-k]
		for i,num in enumerate(numscopy):
			nums[i] = num
s = Solution()
nums = [1,2,3,4,5,6,7]
s.rotate(nums,1)
print nums