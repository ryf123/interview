class Solution(object):
	def convert(self, s, numRows):
		"""
		:type s: str
		:type numRows: int
		:rtype: str
		"""
		l = len(s)
		if numRows == 0:
			return ""
		numCols = l/2+l/numRows+1
		n = [""]*numCols
		m = [n[:] for x in xrange(numRows)]
		p,col = 0,0
		while p <l and col<numCols:
			for i in xrange(numRows):
				if p<l:
					m[i][col] = s[p]
					p+=1
				else:
					break
			# print m
			col+=1
			for i in xrange(numRows-2):
				if p<l:
					m[numRows-2-i][col] = s[p]
					col+=1
					p+=1
				else:
					break
		ret = []
		for row in m:
			ret.append("".join(row))
		return "".join(ret)
sl = Solution()
s = "PAYPALISHIRING"
print len(s)
print sl.convert("PAYPALISHIRING", 1)
print s,"PAHNAPLSIIGYIR"

