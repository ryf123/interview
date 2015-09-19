class Solution:
	# @param {integer[]} nums
	# @param {integer} target
	# @return {boolean}
	def search(self, nums, target):
		l = len(nums)
		ret = -1
		if l > 0:
			ret = self.rotatesearch(nums,0,l-1,target)
		print ret
		if ret == -1:
			return False
		else:
			return True
	def rotatesearch(self,nums,start,end,target):
		if start > end:
			return -1
		mi = (start+end)/2
		mv = nums[mi]
		if mv == target:
			return mi
		if mv > nums[start]: # if middle is greater than nums[start], then lower part is sorted
			if target <= mv and target >= nums[start]:
				ret = self.rotatesearch(nums,start,mi-1,target)
			else: # search upper part
				ret = self.rotatesearch(nums,mi+1,end,target)
		elif mv < nums[start]: # else upper part is sorted
			if target >= mv and target <= nums[end]:
				ret = self.rotatesearch(nums,mi+1,end,target)
			else:
				ret = self.rotatesearch(nums,start,mi-1,target)
		else: #if middle value equals start both side will be searched
			ret1 = self.rotatesearch(nums,mi+1,end,target)
			ret2 = self.rotatesearch(nums,start,mi-1,target)
			if ret1 != -1:
				ret = ret1
			elif ret2 != -1:
				ret = ret2
			else:
				ret = -1
		return ret
s = Solution()
nums = [1,1,3]
target = 3
print s.search(nums,target)