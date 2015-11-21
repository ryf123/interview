class Solution(object):
	def isPowerOfTwo(self, n):
		"""
		:type n: int
		:rtype: bool
		"""
		powertwo = 1
		while powertwo <= n:
			if powertwo == n:
				return True
			powertwo *=2 
		return False