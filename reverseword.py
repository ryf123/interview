class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        s = s.split()
        return " ".join(s[::-1])
s = Solution()
print s.reverseWords("the sky is blue")