class Solution(object):
	def fractionToDecimal(self, numerator, denominator):
		"""
		:type numerator: int
		:type denominator: int
		:rtype: str
		"""
		if denominator == 0:
			return ""

		res = ""
		if numerator < 0 and denominator >0:
			sign = "-"
		elif numerator > 0 and denominator < 0:
			sign = "-"
		else:
			sign = "+"
		numerator,denominator = abs(numerator),abs(denominator)
		res  += str(numerator/denominator)
		
		d = {}
		i = len(res)+1
		
		if numerator%denominator == 0:
			return res if sign == "+" else "-"+res
		else:
			res += "."
		r = numerator%denominator
		
		while r != 0:
			if r in d:
				res = res[:d[r]] + "(" +res[d[r]:] + ")"
				break
			else:
				d[r] = i
				i+=1
				r*=10
				res += str(r/denominator)
				r%=denominator
				# print [r,denominator]
			
		return res if sign == "+" else "-"+res
s = Solution()
tests = [[1,2],[2,1],[2,3]]
for x in xrange(10):
	print x,s.fractionToDecimal(-5000,x)