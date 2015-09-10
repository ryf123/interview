class Solution(object):
	def hIndex(self, citations):
		"""
		:type citations: List[int]
		:rtype: int
		"""
		# citations.sort()
		l = len(citations)
		h = 0
		for i,citation in enumerate(citations):
			if citation >= l-i :
				if h == None:
					h = l-i
				else:
					h = l-i if l-i > h else h
		return h
s = Solution()
citations =  [3, 4, 3, 1, 3]
citations = [3, 0, 6, 1, 5]
# citations = [100]
citations = [1]
print s.hIndex(citations)
