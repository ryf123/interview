class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        nums.sort()
        l = len(nums)
        p1 = 0
        p2 = l-1
        counter = 0
        while(p1<=p2):
            if val == nums[p1]:
                temp = nums[p1]
                nums[p1] = nums[p2]
                nums[p2] = temp
                counter +=1
                if nums[p1] == val:
                    if p1 != p2:
                        counter+=1
                p1+=1
                p2-=1

            else:
                p1+=1
        return l-counter
s = Solution()
nums = [5,2,2,1]
val = 2
l = s.removeElement(nums,val)
print nums[:l]