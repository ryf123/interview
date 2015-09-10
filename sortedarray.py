class Solution:
    # @param {integer[]} nums
    # @return {integer}
	def findMin(self, nums):
		if len(nums) == 1:
			return nums[0]
		min = None
		for i,num in enumerate(nums):
			if i>0:
				if (nums[i-1] > num):
					min = num
					break
		if min == None:
			return nums[0]
		return min

	# @param {integer[]} nums
	# @param {integer} target
	# @return {integer[]}
	def searchRange(self, nums, target):
		ret = [-1,-1]
		start = -1
		end = -1
		l = len(nums)
		if l == 0:
			return ret
		ret = self.binary_search(nums,target,0,l-1)
		if ret != -1:
			start = self.findlowerboundary(nums,target,0,ret-1)
			end = self.findhigherboundary(nums,target,ret+1,l-1)
		if start == -1:
			start = ret
		if end == -1:
			end = ret
		return [start,end]
	def binary_search(self,nums,target,start,end):
		print(start,end)
		if start > end:
			return -1
		l = len(nums)
		pi = (end+start)/2 # index of pivot
		pivot = nums[pi]
		if(pivot > target):
			 ret = self.binary_search(nums,target,start,pi-1)
		elif(pivot < target):
			ret = self.binary_search(nums,target,pi+1,end)
		else:
			ret = pi
		print ret
		return ret
	def findlowerboundary(self,nums,target,start,end):
		print "find low boundary %s %s"%(start,end)
		if start > end:
			return -1
		pi = (end+start)/2 # index of pivot
		pivot = nums[pi]
		if start == end:
			if pivot == target:
				return pi
			else:
				return end+1
		if pivot < target:
			ret = self.findlowerboundary(nums,target,pi+1,end)
			if ret == -1:
				ret = end+1
		elif pivot == target:
			ret = self.findlowerboundary(nums,target,start,pi-1)
			if ret == -1:
				ret = pi
		return ret
	def findhigherboundary(self,nums,target,start,end):
		print "find high boundary %s %s"%(start,end)
		if start > end:
			return -1
		pi = (end+start)/2 # index of pivot
		pivot = nums[pi]
		if start == end:
			if pivot == target:
				return pi
			else:
				return start-1

		if pivot > target:
			ret = self.findhigherboundary(nums,target,start,pi-1)
			if ret == -1:
				ret = start-1
		elif pivot == target:
			ret = self.findhigherboundary(nums,target,pi+1,end)
			if ret == -1:
				ret = pi-1
		return ret
s = Solution()
print s.findMin([1,2])