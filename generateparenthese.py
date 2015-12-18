class Solution:
    # @param {integer} n
    # @return {string[]}
    def generateParenthesis(self, n):
        self.ret = []
        self.generate(n,n,"")
        return self.ret
    def generate(self,left,right,path):
        if left == 0 and right == 0:
            self.ret.append(path)
        if left >0:
            self.generate(left-1,right,path+"(")
        if left < right:
            self.generate(left,right-1,path+")")


s = Solution()
print s.generateParenthesis(3)
