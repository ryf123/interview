class Solution(object):
	def generateParenthesis(self, n):
		"""
		:type n: int
		:rtype: List[str]
		"""
		def putparenthesis(left,right,s):
			# ret = []
			if right==0 and left==0:
				return self.ret.append(s)
			if left < right and right >0:
				# put right one
				sleft = putparenthesis(left,right-1,s+")")
				# for sl in sleft:
				# 	ret.append(s+sl)
			if left >0:
				sright = putparenthesis(left-1,right,s+"(")
				# for sr in sright:
				# 	ret.append(s+sr)

			return self.ret
		self.ret = []
		return putparenthesis(n-1,n,"(")
s = Solution()
print s.generateParenthesis(3)

