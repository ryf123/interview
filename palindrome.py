class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        s = str(x)
        l = len(s)
        for i in range(0,l/2):
            if(s[i] != s[l-i-1]):
                return False
        return True
s = Solution()
print s.isPalindrome("102132101")