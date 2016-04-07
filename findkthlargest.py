class Solution:
	# @param {integer[]} nums
	# @param {integer} k
	# @return {integer}
	def findKthLargest(self, nums, k):
		if len(nums) > 0:
			return self.findk(nums,k) 
	def findk(self,nums,k):
		# print nums,k
		
		l = len(nums)
		if l == 1:
			return nums[0]
		pivot = nums[0]
		start,end = 1,l-1
		while start <= end:
			if nums[start] <= pivot:
				start += 1
			if nums[end] >= pivot:
				end -= 1
			if start < end and nums[start] > pivot and nums[end] <= pivot:
				self.swap(nums,start,end)
		self.swap(nums,end,0)
		# print nums,k
		if l - end  < k:
			return self.findk(nums[:end],k- (l-end))
		elif l - end  > k:
			return self.findk(nums[end+1:],k)
		else:
			return nums[end]
	def swap(self,nums,i,j):
		temp = nums[i]
		nums[i] = nums[j]
		nums[j]  = temp
s = Solution()
nums = [7,6,5,4,3,2,1]
for x in xrange(1,8):
	print s.findKthLargest(nums,x)