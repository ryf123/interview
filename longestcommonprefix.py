class Solution(object):
	def longestCommonPrefix(self, strs):
		"""
		:type strs: List[str]
		:rtype: str
		"""
		l = len(strs)
		if l ==0:
			return ""
		lw = min(len(st) for st in strs)
		
		i = 0
		while i<lw:
			# print i
			c = strs[0][i]
			
			for j in xrange(l):
				# print c,i,j
				if strs[j][i] != c:
					return strs[j][:i]
			i+=1
		return strs[0][:i]
s = Solution()
strs = []
print s.longestCommonPrefix(strs)