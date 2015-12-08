class Solution(object):
	def numTrees(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		if n<=0:
			return 0
		nums = (n+1)*[0]
		nums[0],nums[1] = 1,1
		i = 2
		while i<=n:
			for j in xrange(0,i):
				left = j
				right = i-j-1
				nums[i] += nums[left] * nums[right]
			i+=1 
		return nums[n]
s = Solution()
assert(s.numTrees(1)==1)
assert(s.numTrees(3)==5)