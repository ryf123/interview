class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):
        k = k-1
        ret = ""
        s = [x for x in range(1,n+1)]
        group = [1]*(n+1)
        for i in range(1,n+1):
            group[i] = group[i-1]*i
        for num in group[n-1:0:-1]:
            index = k/num
            ret += str(s[index])
            s.pop(index)
            if k/num >0:
                k-= k/num*num
        return ret+str(s[0])
s = Solution()
print s.getPermutation(3,5)