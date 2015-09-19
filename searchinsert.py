class Solution:
	# @param {integer[]} nums
	# @param {integer} target
	# @return {integer}
	def searchInsert(self, nums, target):
		l  = len(nums)
		if (l == 0):
			return [target]
		ret = self.search(nums,0,l-1,target)
		return ret
	def search(self,nums,start,end,target):
		mi = (start+end)/2
		mv = nums[mi]
		if mv == target:
			return mi
		if start >= end:
			# insert the start meets end
			if target > mv:
				return end+1
			else:
				return start
		# for the normal case where start < end
		if mv < target:
			ret = self.search(nums,mi+1,end,target)
		else:
			ret = self.search(nums,start,mi-1,target)
		return ret
s  = Solution()
print s.searchInsert([1,2,3],0)