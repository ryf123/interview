class Solution(object):
	def longestValidParentheses(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		stack = []
		total = 0
		longest = 0
		valid =0
		start = -1
		for i,p in enumerate(s):
			if p == "(":
				stack.append(i)
			else:
				if not stack:
					start = i
				else:
					stack.pop()
					if len(stack):
						longest = max(i-stack[-1],longest)
					else:
						longest = max(i-start,longest)
		return longest
s = Solution()
st = ["()(()","(()","())","()()"]
for p in st:
	print s.longestValidParentheses(p)		