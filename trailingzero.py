class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<0:
        	return -1
        i = 5
        count = 0
        while(i<=n):
        	count += n/i
        	i*=5
    	return count
s = Solution()
for x in xrange(10):
	x = x*10
	print x,s.trailingZeroes(x)