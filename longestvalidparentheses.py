class Solution(object):
	def longestValidParentheses(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		i,l = 0,len(s)
		count = 0
		maxlen = 0
		currentlen = 0
		while i <l:
			if s[i] == "(":
				count+=1
			elif s[i] == ")":
				if count >0:
					count-=1
					currentlen +=2
					maxlen = max(maxlen,currentlen)
				else:
					currentlen = 0
			i+=1
		return maxlen
tests = [")()())","(()","())","((()))","()(()"]
s = Solution()
for t in tests:
	print s.longestValidParentheses(t)

