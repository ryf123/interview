class Solution(object):
	def getRow(self, numRows):
		"""
		:type numRows: int
		:rtype: List[List[int]]
		"""
		ret = []
		numRows +=1
		for i in xrange(numRows):
			# if i == 0:
			# 	ret.append([1])
			# 	continue
			row = []
			for j in xrange(i+1):
				if j == 0:
					row.append(1)
				elif j == i:
					row.append(1)
				else:
					row.append(ret[j-1]+ret[j])
			ret = row
		return ret
s = Solution()
print s.getRow(3)