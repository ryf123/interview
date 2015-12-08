class Solution(object):
	def isPowerOfTwo(self, n):
		"""
		:type n: int
		:rtype: bool
		"""
		powertwo = 1
		while n:
			if n&1 == 1:
				return True if n==1 else False
			n >>=1
		return False
s = Solution()
assert(s.isPowerOfTwo(4))
assert(s.isPowerOfTwo(1))
assert(not s.isPowerOfTwo(3))