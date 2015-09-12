class Solution(object):
	def isScramble(self, s1, s2):
		"""
		:type s1: str
		:type s2: str
		:rtype: bool
		"""
		if s1 == s2:
			# print s1,s2
			return True
		l,l2 = len(s1),len(s2)
		if l !=l2:
			return False
		if sorted(s1) != sorted(s2):
			return False
		
		for i in range(1,l):
			# print s1,s2
			if self.isScramble(s1[:i],s2[:i]) and self.isScramble(s1[i:],s2[i:]):
				return True
			if self.isScramble(s1[i:],s2[:l-i]) and self.isScramble(s1[:i],s2[l-i:]):
				return True
		return False
s = Solution()
print s.isScramble("abb","bba")
print s.isScramble("xstjzkfpkggnhjzkpfjoguxvkbuopi","xbouipkvxugojfpkzjhnggkpfkzjts")