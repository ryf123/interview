class Solution(object):
	def firstMissingPositive(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		nums.append(0)
		for i,num in enumerate(nums):
			self.swap(nums,num)
		# print nums
		maxval = 0
		for i,num in enumerate(nums):
			if i >=0 :
				if num != i:
					return i
			maxval = max(maxval,num)
		if len(nums)==0:
			return 1
		return maxval+1 if nums[0] != 1 else 2
	def swap(self,nums,num):
		if num < len(nums) and num >=0 and nums[num] != num:
			temp = nums[num]
			nums[num] = num
			if temp >=0:
				self.swap(nums,temp)

s = Solution()
tests = [[3,4,-1,1],[1],[2],[3,1],[-1,0],[],[2,1],[1,2,3]]
for t in tests:
	print t,s.firstMissingPositive(t)