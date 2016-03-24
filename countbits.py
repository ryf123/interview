class Solution(object):
	def countBits(self, num):
		"""
		:type num: int
		:rtype: List[int]
		"""
		if num == 0:
			return [0]
		ret = [0]
		total = 0
		for i in xrange(1,num+1):
			if i & 1 == 0:
				total = ret[i>>1]
			else:
				total += 1
			ret.append(total)
		return ret
s = Solution()
print s.countBits(40)
expected =  [0,1,1,2,1,2,2,3,1,2,2,3,2,3,3,4,1,2,2,3,2,3,3,4,2,3,3,4,3,4,4,5,1,2,2,3,2,3,3,4,2,3,3,4,3,4,4,5,2,3,3]
for i,count in enumerate(expected):
	print i,count