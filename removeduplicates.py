class Solution(object):
	def removeDuplicates(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		l = len(nums)
		if not l:
			return l
		p1 = 0
		# counter = l
		prev = None
		counter = 0
		for i,num in enumerate(nums):
			if num == prev and prev != None:
				counter +=1
				if counter >=2:
					l -=1
				elif counter ==1:
					nums[p1] = num
					p1+=1
				continue
			counter = 0					
			prev = num
			nums[p1] = num
			p1 +=1
		return l
s = Solution()
nums = [1,1,1,1,1,1,1,1,2,2,2,2,3,3,3,3,3]
print s.removeDuplicates(nums)
print nums

