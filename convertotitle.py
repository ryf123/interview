class Solution(object):
	def convertToTitle(self, n):
		ret = ""
		alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		base  = 26
		while n:
			ret = alphabet[(n-1)%26] +ret
			n = (n-1)/26
		return ret 

s = Solution()
for x in range(26,26+28):
	print s.convertToTitle(x)

