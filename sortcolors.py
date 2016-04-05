class Solution:
    def swap(self,nums,i,j):
        if i != j:
            nums[i] = nums[i] ^ nums[j]
            nums[j] = nums[i] ^ nums[j]
            nums[i] = nums[i] ^ nums[j]
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    # red<white<blue
    def sortColors(self, nums):
        pivot = 1
        red_p = 0
        white_p = 0
        blue_p = len(nums) - 1
        while white_p <= blue_p:
            if nums[white_p] == pivot:
                white_p += 1 
            elif nums[white_p] < pivot:
                self.swap(nums,red_p,white_p)
                red_p += 1
                white_p += 1
            else:
                self.swap(nums,blue_p,white_p)
                blue_p -= 1

s = Solution()
nums = [2]
s.sortColors(nums)
print nums            