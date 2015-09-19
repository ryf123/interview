class Solution:
	# @param {integer[]} nums
	# @param {integer} target
	# @return {integer}
	def search(self, nums, target):
		self.nums = nums
		return self.solve(0,len(nums)-1,target)
	def solve(self,start,end,target):
		if start > end:
			return -1
		mid = (start+end)/2
		if self.nums[mid] == target:
			return mid
		if self.nums[start] < self.nums[end]:
			if self.nums[mid] > target:
				return self.solve(start,mid-1,target)
			elif self.nums[mid] < target:
				return self.solve(mid+1,end,target)
		else:
			lret = self.solve(start,mid-1,target)
			if lret != -1:
				return lret
			rret = self.solve(mid+1,end,target)
			if rret != -1:
				return rret
		return -1 
s =  Solution()
nums = [4,5,6,7,8,0,1,2]
print s.search([],0)
for num in nums:
	print num,s.search(nums,num)

