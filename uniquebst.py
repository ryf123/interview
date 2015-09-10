class Solution(object):
	def numTrees(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		nums = [0]*(n+1)
		nums[1] = 1 
		for i in range(2,n+1):
			total = 0
			for j in range(0,i):
				left = nums[j-0] if j >0 else 1
				right = nums[i-j-1] if i-j-1 > 0 else 1
				total += left * right
			nums[i] = total
		return nums[n]
s = Solution()
print s.numTrees(1)