class Solution(object):
	def titleToNumber(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		s = s[::-1]
		total = 0
		alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
		for i,c in enumerate(s):
			index = alphabet.index(c)+1
			total+= index*pow(26,i)
		return total