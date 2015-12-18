class Solution(object):
	def canWinNim(self, n):
		"""
		:type n: int
		:rtype: bool
		"""
		# a,b,c = False,False,False
		# for x in range(1,n+1):
		# 	current = False
		# 	if a == False:
		# 		current = True
		# 	if b == False:
		# 		current = True
		# 	if c == False:
		# 		current = True
		# 	a,b,c = current,a,b
		# return a
		return n%4 !=0
s = Solution()
for x in xrange(10):
	print s.canWinNim(x)
