class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        
	def searchinsortarray(nums,target):
		ln = len(nums)
		pivot = ln/2
		if (target > nums[pivot]):
			self.searchinsortarray(nums[pivot:ln],target)
		elif(target < nums[pivot]):
			self.searchinsortarray(nums[0:pivot],target)
		elif(target == nums[pivot]):
			