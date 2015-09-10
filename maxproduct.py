class Solution(object):
	def maxProduct(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if len(nums) == 0:
			return
		res = nums[0]
		maxnum= nums[0]
		minnum = nums[0]
		for x in nums[1:]:
			tempmaxnum = maxnum
			tempminnum = minnum
			maxnum = max([tempminnum*x,tempmaxnum*x,x])
			minnum = min([tempmaxnum*x,tempminnum*x,x])
			# print maxnum,minnum,res
			res = max(res,maxnum)
		return res
s= Solution()
nums = [-1,-2,-3,-4]
print s.maxProduct(nums)





