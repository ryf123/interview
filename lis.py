class Solution(object):
	def lengthOfLIS(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		l = len(nums)
		if l == 0:
			return 0
		i = l-1
		lis = [1]*l
		while i:
			num = nums[i]
			j = i+1
			while j<l-1:
				if nums[j] > num:
					lis[i] = max(lis[i],lis[j]+1)
				j+=1
			i-=1
		return max(lis)
s = Solution()
nums = [10, 9, 2, 5, 3, 7, 101, 18]
nums = []
print s.lengthOfLIS(nums)