class Solution(object):
    def rob(self, nums):
        l = len(nums)
        if l== 0:
            return 0
        if l ==1:
            return nums[0]
        return max(self.robone(nums[:l-1]),self.robone(nums[1:]))
    def robone(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 0:
        	return 0
        total = [0] * l
        for i in range(0,l):
        	beforeprev =  total[i-2] if i>=2 else 0
        	prev = total[i-1] if i>=1 else 0
        	total[i] = max(beforeprev+nums[i],prev)
    	return total[l-1]
s = Solution()
print s.rob([1,2,3])