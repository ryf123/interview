class Solution(object):
	def getRow(self, numRows):
		"""
		:type numRows: int
		:rtype: List[List[int]]
		"""
		if numRows < 0:
			return []
		for i in xrange(numRows+1):
			temp  = []
			if i == 0:
				row = [1]
			else:
				for j in xrange(i+1):
					a = row[j-1] if i-1>=0 and j-1>=0 else 0
					b = row[j] if i-1>=0 and j<i else 0
					temp.append(a+b)
				row = temp
		return row
s = Solution()
print s.getRow(3)