class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        def compare(s1,s2):
            return (-1 if s1+s2 > s2+s1 else 1)
        numsstring = map(str,nums)
        ret =  "".join(sorted(numsstring,cmp=compare))
        return ret.lstrip("0") or "0"
s = Solution()
print s.largestNumber([0])