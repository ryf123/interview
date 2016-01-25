from collections import OrderedDict
class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        d  = OrderedDict()
        max = 0
        count = 0
        for l in s:
            if l not in d:
                d[l] = True
                if max < count:
                    max = count
            else:
                while l in d:
                    d.popitem(last=False)
                    count -=1
                d[l] = True
            count +=1
        return max