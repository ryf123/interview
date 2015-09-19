from itertools import permutations
class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):
        k = k-1
        s = range(1,n+1)
        s = map(str,list(s))
        ret = []
        while len(s) > 0:
            l = len(s)
            total = 1
            for i in range(1,l):
                total *=i
            if k > total*l:
                return ""
            index = k/total
            ret.append(s[index])
            s.pop(index)
            k = k- (k/total)*total
        return "".join(ret)
s = Solution()
print s.getPermutation(9,27000)