class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def firstMissingPositive(self, nums):
        maxnum = max(nums)
        minnum = min(nums)
        sumnum = sum(nums)
        l = len(nums)
        sumnomiss = (minnum + maxnum -1)*(l)/2
        return sumnomiss-sumnum + maxnum
s = Solution()
nums = [3,4,-1,1]
print s.firstMissingPositive(nums)