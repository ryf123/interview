class Solution(object):
	def simplifyPath(self, path):
		"""
		:type path: str
		:rtype: str
		"""
		paths = path.split("/")
		stack = []
		for p in paths:
			if p:
				if p == ".":
					continue
				elif p == "..":
					if len(stack) >0:
						stack.pop()
				else:
					stack.append(p)
		print stack
		return "/"+"/".join(stack)
s = Solution()
print s.simplifyPath("/home//foo/")
