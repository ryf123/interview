import sys
class Solution(object):
	def findPeakElement(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		l = len(nums)
		assert(l>=3)
		start,end = 1,l-2
		return self.findPeakElement(start,end)
	def binarysearch(self,start,end):
		if start == end:
			return start
		mid = (start+end)/2
		left,right,num = nums[mid-1],nums[mid+1],nums[mid]
		if mid <right:
			return self.binarysearch(mid+1,end)
		elif mid<left:
			return self.binarysearch(start,mid-1)
		else:
			return mid

