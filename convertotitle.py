class Solution(object):
	def convertToTitle(self, n):

		alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
		base =1
		res = ""
		while n:
			res += alphabet[(n-1)%26] 
			n = (n-1)/26
		return res[::-1]
s = Solution()
for x in range(26*26,26*26+28):
	print s.convertToTitle(x)

