class Solution(object):
	def isValid(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		pairs = ["()","[]","{}"]
		d = {}
		validsymbol = {}
		stack = []
		for pair in pairs:
			d[pair[1]] = pair[0]
			validsymbol[pair[1]] = True
			validsymbol[pair[0]] = True

		for c in s:
			if c not in validsymbol:
				return False
			if c in d:
				if len(stack) == 0:
					return False
				if stack.pop() != d[c]:
					return False
			else:
				stack.append(c)
		return len(stack)==0


s = Solution()
print s.isValid("()[){}")