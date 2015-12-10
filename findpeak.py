import sys
class Solution(object):
	def findPeakElement(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		self.nums = nums
		return self.find(0,len(nums))
	def find(self,start,end):
		if start == end:
			return start
		mid = (start+end)/2
		prev = self.nums[mid-1] if mid>0 else -sys.maxint
		next = self.nums[mid+1] if mid+1< len(self.nums) else -sys.maxint
		if self.nums[mid] < prev:
			return self.find(start,mid-1)
		elif self.nums[mid] < next:
			return self.find(mid+1,end)
		else:
			return mid