class Solution(object):
	def longestConsecutive(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		d = {}
		maxlen = 0
		for num in nums:
			d[num] =True
		for key in d:
			if d[key]:
				d[key] = False
				start,end = key-1,key+1
				start_in = start in d
				end_in = end in d
				while start_in or end_in:
					if start in d:
						d[start] = False
						start-=1
						start_in = start in d
					if end in d:
						d[end] = False
						end+=1
						end_in = end in d 
				maxlen = max(end-start-1,maxlen)
		return maxlen


s = Solution()
print s.longestConsecutive([100, 4, 200, 1, 3, 2,0,-1])
