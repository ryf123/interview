class Solution(object):
	def isInterleave(self, s1, s2, s3):
		"""
		:type s1: str
		:type s2: str
		:type s3: str
		:rtype: bool
		"""
		l1 = len(s1)
		l2 = len(s2)
		l3 = len(s3)
		self.l1 = l1
		self.l2 = l2
		self.l3 = l3
		self.s1 = s1
		self.s2 = s2
		self.s3 = s3
		self.dp = [[1]*(l2+1) for x in xrange(l1+1)]
		return self.dfs(0,0,0)
	def dfs(self,start1,start2,start3):
		# print start1,start2,start3,self.dp
		if self.dp[start1][start2] == 0:
			return False
		if start3 == self.l3:
			if (start1 == self.l1 and start2 == self.l2):
				return True
			else:
				self.dp[start1][start2] = 0
				return False
		if start1<self.l1 and self.s1[start1] == self.s3[start3]:
			if self.dfs(start1+1,start2,start3+1):
				return True
		if start2<self.l2 and self.s2[start2] == self.s3[start3]:
			if  self.dfs(start1,start2+1,start3+1):
				return True
		self.dp[start1][start2] = 0
		return False
s = Solution()
s1,s2,s3 = "abab","bbbb","bbabba"
s1,s2,s3 = "b","ba","bba"
print s.isInterleave(s1,s2,s3)


