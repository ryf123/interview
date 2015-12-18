class Solution(object):
	def isMatch(self, s, p):
		"""
		:type s: str
		:type p: str
		:rtype: bool
		"""
		lp = len(p)
		i = 0
		if lp == 0:
			return len(s) == 0 
		ls = len(s)
		j = 0
		star = False
		starpos = -1
		while j<ls:
			if (i<lp and j<ls) and (p[i] == s[j] or p[i] == "?"):
				i+=1
				j+=1
			else:
				if i<lp and p[i] == "*":
					starpos = i
					jIndex = j
					star = True
					i+=1
				elif star:
					j = jIndex +1
					i = starpos+1
					jIndex +=1
				else:
					return False
		while i<lp and p[i] == "*":
			i+=1
		return i==lp
s = Solution()
assert(s.isMatch("aa","a")==False)
assert(s.isMatch("aa","aa"))
assert(s.isMatch("aaaa", "*"))
assert(s.isMatch("aa", "a*"))
assert(s.isMatch("ab", "*?"))
assert(s.isMatch("aab", "c*a*b")==False)
assert(s.isMatch("c", "*?*"))