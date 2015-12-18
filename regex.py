class Solution(object):
	def isMatch(self, s, p):
		"""
		:type s: str
		:type p: str
		:rtype: bool
		"""
		i = len(p)-1
		j = len(s)-1
		if i ==-1:
			return j==-1
		star = False
		while j>=0:
			if i>=0 and (p[i] == s[j] or p[i] == "."):
				i-=1
				j-=1
			elif i>=0 and p[i] == "*":
				if i == 0:
					break
				if self.isMatch(s[:j+1],p[:i-1]):
					return True
				if i-1>=0 and (p[i-1] =="."  or p[i-1] ==s[j]):
					j-=1
					i-=1
					star = True
					starPos = i
				else:
					return False
			elif star:
				if p[starPos] == s[j] or p[starPos] == ".":
					i = starPos 
			else:
				return False
		star = False
		while i>=0 and p[i] =="*":
			star = True
			i-=1
		return i == -1 or (star and i==0)


s = Solution()
assert(s.isMatch("aa","a")==False)
assert(s.isMatch("aa","aa"))
assert(s.isMatch("aaa", ".*"))
assert(s.isMatch("aa", "a*"))
assert(s.isMatch("ab", ".*"))
assert(s.isMatch("bbbba", ".*a*a"))
assert(s.isMatch("aa", "c*a*"))