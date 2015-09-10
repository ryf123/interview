class Solution(object):
	def combine(self, n, k):
		"""
		:type n: int
		:type k: int
		:rtype: List[List[int]]
		"""
		def findcomb(num,left,comb):
			if left == 0:
				self.ret.append(comb)
			for i,x in enumerate(num):
				findcomb(num[i+1:],left-1,comb+[x])
		nums = [x for x in range(1,n+1)]
		self.ret = []
		findcomb(nums,k,[])
		return self.ret
s = Solution()
print s.combine(3,4)
