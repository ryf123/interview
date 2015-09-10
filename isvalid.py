class Solution(object):
	def isValid(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		stack = []
		for x in s:
			if x == ")":
				if stack:
					if stack.pop() != "(":
						return False
				else:
					return False
			elif x =="]":
				if stack:
					if stack.pop() != "[":
						return False
				else:
					return False
			elif x == "}":
				if stack:
					if stack.pop() != "{":
						return False
				else:
					return False
			else:
				stack.append(x)
			print stack
		print stack
		if stack:
			return False
		else:
			return True
s = Solution()
print s.isValid("()[]{}")