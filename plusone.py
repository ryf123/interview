class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        l = len(digits)
        i = l-1
        while i>=0:
        	if digits[i] == 9:
        		digits[i] = 0
    		else:
    			digits[i] +=1
    			return digits
        	i-=1
    	return [1]+digits if len(digits) else []
digits = [1,2,3,4,5]
sl = Solution()
print sl.plusOne(digits)
digits = [9,9,9]
print sl.plusOne(digits)
digits = [1,9]
print sl.plusOne(digits)
digits = []
print sl.plusOne(digits)