class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def majorityElement(self, nums):
        l = len(nums)
        n1 =  n2 = None
        c1 = c2= 0
        for n in nums:
            if n == n1:
                c1+=1
            elif n==n2:
                c2+=1
            elif c1 == 0:
                n1 = n
                c1 = 1
            elif c2==0:
                n2 = n
                c2 =1
            else:
                c1-=1
                c2-=1
            print n1,c1,n2,c2
        return [n for n in [n1,n2] if n is not None and nums.count(n)>l/3]
nums = [1,1,1,3,3,2,2,2]
s = Solution()
print s.majorityElement(nums)