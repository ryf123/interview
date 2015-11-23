class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        num = 1
        total = 1
        if n == 0:
        	return 1
    	neg = False
        if n <0:
        	n = abs(n)
        	neg = True
        while n:
        	if n == 1:
        		total *=x
        		break 
        	tempnum = 1
        	temptotal = x
        	while tempnum*2 <=n:
        		tempnum *=2
        		temptotal *= temptotal
    		total *= temptotal
    		n -= tempnum
    	return 1.0/total if neg else total
s = Solution()
assert(pow(2,-3) == s.myPow(2,-3))
assert(pow(0,100) == s.myPow(0,100))


