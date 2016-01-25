class Solution(object):
	def convert(self, s, numRows):
		"""
		:type s: str
		:type numRows: int
		:rtype: str
		"""
		l = len(s)
		i = 0
		matrix = [[] for x in xrange(numRows)]
		while i<l:
			j = 0
			while j<numRows and i<l:
				matrix[j].append(s[i])
				i+=1
				j+=1
			j = numRows -2
			while j >0 and i<l:
				matrix[j].append(s[i])
				i+=1
				j-=1
		ret = ""
		for row in matrix:
			ret += "".join(row)
		return ret
sl = Solution()
s = "PAYPALISHIRING"
print len(s)
assert(sl.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR") 

