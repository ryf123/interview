class Solution:
	# @param {integer[]} nums
	# @param {integer} target
	# @return {integer[]}
	def searchRange(self, nums, target):
		self.start,self.end = -1,-1
		self.binarysearch(nums,target)
		self.binarysearch(nums,target,lower_part=False)
		return [start,end]
	def binarysearch(self,nums,target,lower_part=True):
		l = len(nums)-1
		start,end = 0,l
		while start<=end:
			mid = (start+end)/2
			if nums[mid]>target:
				end = mid-1
			elif nums[mid] < target:
				start = mid+1
			else:
				if lower_part:
					if mid == 0 or (nums[mid-1] < nums[mid]):
						self.start = mid
						return
					else:
						end = mid-1
				else:
					if mid == l or (nums[mid+1] > nums[mid]):
						self.end = mid
						return
					else:
						start +=1


