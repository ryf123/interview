class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = map(str,digits)
        s = "".join(digits)
        ret =  list(str(int(s)+1))
        return map(int,ret)
digits = [1,2,3,4,5]
sl = Solution()
print sl.plusOne(digits)