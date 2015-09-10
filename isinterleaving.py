class Solution(object):
	def isInterleave(self, s1, s2, s3):
		"""
		:type s1: str
		:type s2: str
		:type s3: str
		:rtype: bool
		"""
		l1,l2,l3 = len(s1),len(s2),len(s3)
		if l1+l2 != l3:
			return False
		match = [[False]*(l2+1) for x in xrange(l1+1)] #l1 is row l2 is column
		match[0][0] = True
		for x in range(1,l1+1):
			if s1[x-1] == s3[x-1]:
				match[x][0] = True
			else:
				break
		for y in range(1,l2+1):
			if s2[y-1] == s3[y-1]:
				match[0][y] = True
			else:
				break
		for x in range(1,l1+1):
			for y in range(1,l2+1):
				if s1[x-1] == s3[x+y-1]:
					match[x][y] = match[x-1][y]
				if s2[y-1] == s3[x+y-1]:
					if match[x][y] == False:
						match[x][y] = match[x][y-1]
		# print match
		return match[l1][l2]
s = Solution()
s1,s2,s3 = "db","b","cbb"
print s.isInterleave(s1,s2,s3)


