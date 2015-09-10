class Solution(object):
	def multiply(self, num1, num2):
		"""
		:type num1: str
		:type num2: str
		:rtype: str
		"""
		total = 0
		base = 1
		for m in num2[::-1]:
			ret = self.submultiply(num1,m)
			total += ret*base
			# print total,base,m,ret
			base*=10

		return str(total)
	def submultiply(self,num1,m):
		addon = 0
		total = 0
		base =1
		for n in num1[::-1]:

			mulvalue = int(m) * int(n) + addon
			addon = mulvalue/10
			value = mulvalue%10
			total += value*base
			# print n,num1,total,base
			base*=10
		total += addon*base
		return total
s = Solution()
tests = [["555","444"],["0","100"],["328","642"],["1","1"],["12312312312312312","1231231312312"]]
for t in tests:
	num1,num2 = t
	val = s.multiply(num1,num2) 
	if eval(num1+"*"+num2) != int(val):
		print val,num1,num2,eval(num1+"*"+num2)