class Solution(object):
	def reverseBits(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		s = str(bin(n)[2:])
		l = len(s)
		i = l
		while i<32:
			s = "0"+s
			i+=1
		total = 0
		base = 1
		for num in s:
			if num == "1":
				total += base
			base*=2
		return total
s = Solution()
print s.reverseBits(43261596)

