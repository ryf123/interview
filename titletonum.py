class Solution(object):
	def convertToTitle(self, n):

		alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
		base = 1
		i = 0
		total = []
		n = int(n)
		while n/26:
			total.append(n%26)
			n = n/26
		total.append(n%26)
		ret = ""
		print total
		for n in total:
			ret += alphabet[n-1]
		return ret[::-1]

s = Solution()
tests = ["25","26","27","28","53"]
for t in tests:
	print s.convertToTitle(t)