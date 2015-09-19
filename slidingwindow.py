class Solution:
	# @param {integer[]} nums
	# @param {integer} k
	# @return {integer[]}
	def maxSlidingWindow(self, nums, k):
		ret  = []
		l = len(nums)
		for j in range(0,l-k+1):
			maxnum = max(nums[j:j+k])
			ret.append(maxnum)
		return ret
s = Solution()
nums = [1,3,-1,-3,5,3,6,7]
print s.maxSlidingWindow(nums,3)