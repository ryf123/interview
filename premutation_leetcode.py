class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permute(self, nums):
        ret = []
        l_num = len(nums)
        checked = [0]*l_num
        for index in range(0,l_num):
            if checked[index] ==0:
                checked[index] =1
                results = self.permutation(nums[1:],checked)
                for result in results:
                    ret.append(nums[index]+result)
        return ret
    def permutation(nums,checked):
        ret = []
        l_num = len(nums)
        if l_num ==1:
            return nums
        for index in range(0,l_num):
            if checked[index] ==0:
                checked[index] = 1
                results = self.permutation(nums[1:],checked)
                for result in results:
                    ret.append(nums[index]+result)
        return ret