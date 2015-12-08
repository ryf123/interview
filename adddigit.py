class Solution(object):
	def addDigits(self, num):
		"""
		:type num: int
		:rtype: int
		"""
		if num>=9 and num % 9 == 0:
			return 9
		return num-num/9*9
s= Solution()
assert(s.addDigits(49)==4)
assert(s.addDigits(38)==2)
assert(s.addDigits(9)==9)
assert(s.addDigits(9)==9)   