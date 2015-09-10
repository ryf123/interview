class Solution(object):
	def addDigits(self, num):
		"""
		:type num: int
		:rtype: int
		"""
		num = str(num)
		
		if len(num) >1:
			while(len(num) >1):
				total = 0
				for n in num:
					total+=int(n)
				num = str(total)
		else:
			return int(num)
		return total
s= Solution()
print s.addDigits(49)