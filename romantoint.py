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
		total = 0
		l = len(s)
		characters = list(s)
		for i in xrange(l):
			c = characters[i]
			if i+1 < l and d[c] < d[characters[i+1]]:
				total -= d[c]
			else:

				total += d[c]
		return total

tests = "LIV"
tests = tests.split(", ")
s = Solution()
for t in tests:
	print t,s.romanToInt(t)


