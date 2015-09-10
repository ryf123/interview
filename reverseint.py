class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        minus = 0
        if x< 0:
            minus =1
        s = str(abs(x))
        reverse =  s[::-1]
        if(minus):
            reverse = "-"+reverse
        reverse = int(reverse)
        overflow = pow(2,31)
        if reverse > overflow  or reverse < 0-overflow:
            return 0
        return reverse
s = Solution()
print s.reverse(1)