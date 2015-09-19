class Solution:
	# @param {integer[]} nums
	# @param {integer} target
	# @return {integer}
	def search(self, nums, target):
		l = len(nums)
		rotate = self.findrotate(nums,0,l-1)
		print rotate
		if rotate == -1:
			ret = self.findvalue(nums,0,l-1,target)
		else:
			if target >= nums[rotate] and target <= nums[-1]:
				ret = self.findvalue(nums,rotate,l-1,target)
			elif target <= nums[rotate-1] and target >= nums[0]:
				ret = self.findvalue(nums,0,rotate-1,target)
			else:
				return -1
		return ret
	def findvalue(self,nums,start,end,target):
		l = len(nums)
		if start > end:
			return -1
		mi = (start+end)/2
		mv = nums[mi]
		if mv > target:
			ret = self.findvalue(nums,start,mi-1,target)
		elif mv < target:
			ret = self.findvalue(nums,mi+1,end,target)
		else:
			ret = mi
		return ret 
	def findrotate(self,nums,start,end):
		if start > end:
			return -1
		sv = nums[0]
		mi =  (start+end)/2
		mv =  nums[mi]
		# print (sv,mv,mi,nums)
		if mv >= sv:
			
			ret = self.findrotate(nums,mi+1,end)
		else:
			if mi - 1 >= 0:
				if nums[mi-1] > mv:
					return mi
				ret = self.findrotate(nums,start,mi-1)
			else:
				ret = -1
		return ret
s = Solution()
print s.search([1],1)