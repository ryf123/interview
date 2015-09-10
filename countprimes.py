class Solution(object):
	def countPrimes(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		total = 0
		if n<3:
			return 0
		nums = [1] * n
		nums[0],nums[1] = 0,0
		i = 2
		while(i*i<n):
			if nums[i]:
				# total+=1
				j = 2
				while(j*i<n):
					# print i,j
					nums[j*i] = 0
					j+=1
			i+=1
		return sum(nums)
s = Solution()
tests = range(1500000,1500001)
for t in tests:
	print s.countPrimes(t)
	print "============="

