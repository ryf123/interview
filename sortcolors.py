class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def sortColors(self, nums):
        d = [0]*3
        for i,num in enumerate(nums):
            d[num] +=1
    	i = 0
    	# print d 
    	for color in xrange(3):
	    	while(d[color] > 0):
	    		nums[i] = color
	    		d[color] -=1
	    		i+=1
s = Solution()
nums = [2,2,2]
s.sortColors(nums)
print nums            