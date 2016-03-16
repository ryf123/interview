class Solution(object):
	def moveZeroes(self, nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		p1 = 0
		p2 = 0
		l = len(nums)
		while p2 < l:
			if nums[p2] != 0:
				nums[p1] = nums[p2]
				p1 += 1
			p2 += 1
		while p1 < l:
			nums[p1] = 0
			p1 += 1
a = [0,1,0,2]
s = Solution()

s.moveZeroes(a)
print a