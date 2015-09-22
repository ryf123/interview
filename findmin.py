import sys
class Solution(object):
	def findMin(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		self.l = len(nums)
		return self.solve(0,len(nums)-1,nums)
	def solve(self,start,end,nums):
		# print start,end
		if start > end:
			return sys.maxint
		if nums[end] > nums[start]: # the num is sorted, it can't be equal cause it may be 4,5,6,4 start==end, but not sorted
			return nums[start]
		else:
			mid = (start+end)/2
			if mid+1 < self.l and nums[mid+1] < nums[mid]:
				return nums[mid+1]
			return min(self.solve(start,mid-1,nums),self.solve(mid+1,end,nums),nums[mid])
tests = [[2,1],[1,2,3],[3,2,1],[4,6,7,1,2,3],[2,3,4,5,6,7,1,1,1],[4,5,6,3,4],[3,4,5,6,7,2,2,2,2,2,1]]
s = Solution()
for t in tests:
	print t,s.findMin(t)