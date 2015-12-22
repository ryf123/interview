from collections import Counter
class Solution(object):
	def removeDuplicateLetters(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		# s = list(s)
		if len(s) == 0:
			return ""
		d = Counter()
		pos = 0
		for i,c in enumerate(s):
			d[c]+=1
		for i,c in enumerate(s):
			if c < s[pos]:
				pos = i
			if d[c] == 1:
				break
			d[c] -=1
		return s[pos]+self.removeDuplicateLetters(s[pos+1:].replace(s[pos],"")) 

s = Solution()
tests = ["abcacb","bcabc","","cbacdcbc"]
for t in tests:
	print t,s.removeDuplicateLetters(t)

