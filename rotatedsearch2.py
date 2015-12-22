class Solution:
	# @param {integer[]} nums
	# @param {integer} target
	# @return {boolean}
	def search(self, nums, target):
		l = len(nums)
		start,end = 0,l-1
		while True:
			if start > end:
				return -1
			mi = (start+end)/2
			mv = nums[mi]
			if mv == target:
				return mi
			if mv > nums[start]: # if middle is greater than nums[start], then lower part is sorted
				if target <= mv and target >= nums[start]:
					end = mi-1
					continue
				else: # search upper part
					start = mi + 1
					continue
			elif mv < nums[start]: # else upper part is sorted
				if target >= mv and target <= nums[end]:
					start = mi+1
					continue
				else:
					end = mi-1
					continue
			else: #if middle value equals start, start == end
				if start == mi:
					start = mi+1
				elif end == mi:
					end = mi-1
				else:
					return -1
		return -1
s = Solution()
nums = [1,3]
nums = [1,2,3,4]
target = 3
print s.search(nums,target)