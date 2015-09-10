class Solution(object):
	def summaryRanges(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[str]
		"""
		ret = []
		start = None
		end = None
		for i,num in enumerate(nums):
			if start == None:
				start = num
				end = num
			else:
				if num - nums[i-1] == 1:
					end=num
				else:
					if start ==end or end == None:
						ret.append(str(start))
					else:
						ret.append("%s->%s"%(str(start),str(end)))
					start = num
					end = None

		if start!=None and end == None:
			ret.append(str(num))
		elif start!=None and end!=None:
			if start ==end:
				ret.append(str(start))
			else:
				ret.append("%s->%s"%(str(start),str(end)))
		# if start == None:

		return ret
s = Solution()
nums = [[1,3,9],[1],[1,2,3],[1,2,5,9,10]]
for num in nums:
	print s.summaryRanges(num)
