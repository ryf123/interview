class Solution(object):
	def isMatch(self, s, p):
		"""
		:type s: str
		:type p: str
		:rtype: bool
		"""
		ls,lp = len(s),len(p)
		if lp == 0:
			return ls == 0
		ps = ls-1
		pp = lp-1
		if ls and (s[ps] == p[pp] or p[pp] == "."):
			return self.isMatch(s[:ps],p[:pp])
		elif p[pp] == "*":
			if ls:
				if pp-1>=0 and (p[pp-1] == "." or p[pp-1] == s[ps]):
					return self.isMatch(s,p[:pp-1]) or self.isMatch(s[:ps],p)
			return self.isMatch(s,p[:pp-1])
		return False



s = Solution()
assert(s.isMatch("aa","a")==False)
assert(s.isMatch("aa","aa"))
assert(s.isMatch("aaa", ".*"))
assert(s.isMatch("aa", "a*"))
assert(s.isMatch("ab", ".*"))
assert(s.isMatch("bbbba", ".*a*a"))
assert(s.isMatch("aa", "c*a*"))