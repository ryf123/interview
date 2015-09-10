class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        a = s.split()
        if a:
        	return len(a[-1])
    	else:
    		return 0
s = Solution()
print s.lengthOfLastWord(" ")
        