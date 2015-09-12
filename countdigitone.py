class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        m=1
        ones = 0
        while m<=n:

        	a,b = n/m,n%m
        	ones += (a+8)/10*m
        	if a%10==1:
        		ones+= b+1
        	m*=10
    	return ones
s = Solution()
for x in xrange(1,20):
	print x,s.countDigitOne(x)