class Solution(object):
	def grayCode(self, n):
		"""
		:type n: int
		:rtype: List[int]
		"""
		if n < 0:
			return []
		if n == 0:
			return [0] 
		ret = self.greyString(n)
		# for r in ret:
		# 	print r
		return [int(x, 2)for x in ret]
	def greyString(self,n):
		if n ==1:
			return ["0","1"]
		else:
			ret = self.greyString(n-1)
			current_ret  = []
			for r in ret:
				current_ret.append("0"+r)
			for r in ret[::-1]:
				current_ret.append("1"+r)
			return current_ret
s = Solution()
print s.grayCode(2)

