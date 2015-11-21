class Solution:
    # @param {integer} n
    # @return {string[]}
    def generateParenthesis(self, n):
    	if n == 0:
    		return []
    	self.result = []
    	self.genereate(n,n,"")
    	return self.result
    def genereate(self,left,right,path):
    	if left == 0 and right == 0:
    		self.result.append(path)
        if left <right and right >0:
        	self.genereate(left,right-1,path+")")
        if left > 0:
    		self.genereate(left-1,right,path+"(")
s = Solution()
print s.generateParenthesis(0)
