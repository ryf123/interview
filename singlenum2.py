class Solution(object):
	def singleNumber(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		d = {}
		for num in nums:
			if num in d:
				d[num] +=1
			else:
				d[num] = 1
			if d[num] == 2:
				del d[num]
		ret = []
		for key in d:
			ret.append(key)
		return ret
s = Solution()
print s.singleNumber([1,1,2,3])