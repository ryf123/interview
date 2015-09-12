class Solution(object):
	def divide(self, dividend, divisor):
		"""
		:type dividend: int
		:type divisor: int
		:rtype: int
		"""
		if divisor == 0:
			return 2147483647

		ret = self.conmpute(abs(dividend),abs(divisor),0)

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
	def conmpute(self,dividend,divisor,sol):
		if sol >= 2147483648:
			return 2147483648
		if divisor > dividend:
			return sol
		if divisor <= dividend and (divisor << 1) > dividend:
			return sol +1
		current = divisor
		currentcol = 0
		while(True):
			# print dividend,current,currentcol
			current <<=1
			if current <= dividend:
				if currentcol ==0:
					currentcol =2
				else:
					currentcol *=2
			else:
				current = current >>1
				dividend = dividend - current
				# if dividend >= divisor:
				# 	currentcol +=1
				# print sol,currentcol,dividend,divisor
				return self.conmpute(dividend,divisor,sol+currentcol)
s = Solution()
# div = -5
# for x in range(3,10000):
# 	if s.divide(x,div) != x/div:
# 		print x,s.divide(x,div),x/div
print s.divide(-2147483648,-1)
print s.divide(-2147483650, 1)
print s.divide(1026117192, -874002063)
print s.divide(-1039162657, 490823224)