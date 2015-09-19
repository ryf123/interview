class Solution:
	# @param {integer[]} nums
	# @return {integer[]}
	def productExceptSelf(self, nums):
		leftproduct =[]
		rightproduct = []
		l = len(nums)
		total = 1
		for i in range(0,l):
			leftproduct.append(total)
			if total == 1:
				total = nums[i]
			else:
				total *= nums[i]
		total = 1
		for i in range(1,l+1):
			rightproduct.append(total)
			if total == 1:
				total = nums[l-i]
			else:
				total *= nums[l-i]
		ret = []
		for i in range(0,l):
			product = leftproduct[i] * rightproduct[l-i-1]
			ret.append(product)
		return ret
s = Solution()
print s.productExceptSelf([0,2,3,4])
