class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        l = len(nums)
        end = l
        for i in range(0,l):
            num = nums[l-i-1]
            if num == val:
                nums[l-i-1] = nums[end-1]
                end -=1
        return end if end > 0 else 0
s = Solution()
nums = []
val = 2
l = s.removeElement(nums,val)
print nums[:l]