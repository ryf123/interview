class Solution(object):
	def isIsomorphic(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: bool
		"""
		if len(s) != len(t):
			return False
		d = {}
		mapped = {}
		for i,c in enumerate(s):
			if c not in d:
				d[c] = t[i]
				if t[i] in mapped:
					return False
				mapped[t[i]] = True
			else:
				if t[i] != d[c]:
					return False
		return True
s = Solution()
tests= [["egg","add"],["foo","bar"],["","a"],["ab","aa"]]
for t in tests:
	print s.isIsomorphic(t[0],t[1])
