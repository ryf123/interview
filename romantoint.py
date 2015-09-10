class Solution(object):
	def romanToInt(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		d = {}
		symbols = ["M","D","C","L","X","V","I"]
		value = [1000,500,100,50,10,5,1]
		for i,symbol in enumerate(symbols):
			d[symbol] = value[i]
		total  = 0
		prev = None
		for symbol in s[::-1]:

			if prev != None:
				# print symbols.index(prev),prev
				if symbols.index(prev) < symbols.index(symbol):
					total-= d[symbol]
				else:
					total += d[symbol]
			else:
				total += d[symbol]
			prev = symbol
		return total
tests = "LVIII"
tests = tests.split(", ")
s = Solution()
for t in tests:
	print t,s.romanToInt(t)


