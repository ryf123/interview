class Solution(object):
	def divide(self, dividend, divisor):
		"""
		:type dividend: int
		:type divisor: int
		:rtype: int
		"""
		if divisor == 0:
			return 2147483647

		ret = self.conmpute(abs(dividend),abs(divisor))

		if dividend < 0 and divisor > 0:
			if abs(dividend) % abs(divisor):
				return 0-ret
			else:
				return 0-ret
		elif divisor < 0 and dividend > 0:
			# print ret
			if abs(dividend) % abs(divisor):
				return 0-ret
			else:
				return 0-ret
		else:
			if ret >= 2147483647:
				return 2147483647
			else:
				return ret
	def conmpute(self,dividend,divisor):
		sol = 0
		while dividend >= divisor:
			shift = 0
			currentdivisor = divisor
			while dividend >= currentdivisor<<1:
				currentdivisor <<=1
				shift +=1
			sol += 1<<shift 
			dividend -= divisor<<shift
			if sol >= 2147483648:
				return 2147483648
		return sol

s = Solution()
div = -3
for x in range(3,100):
	if s.divide(x,div) != x/div:
		print x,s.divide(x,div),x/div
# print s.divide(-2147483648,-1)
# print s.divide(-2147483650, 1)
# print s.divide(1026117192, -874002063)
# print s.divide(-1039162657, 490823224)