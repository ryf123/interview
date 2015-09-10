class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for t in tokens:
            if t == "+":
                stack.append(int(stack.pop())+int(stack.pop()))
            elif t == "*":
                stack.append(int(stack.pop())*int(stack.pop()))
            elif t=="-":
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a-b)
            elif t== "/":
                b = int(stack.pop())
                a = int(stack.pop())
                if a*b<0 and a%b !=0:
                    stack.append(a/b+1)
                else:
                    stack.append(a/b)
            else:
                stack.append(t)
            print stack
        return int(stack.pop())
s = Solution()
print s.evalRPN(["4","-2","/","2","-3","-","-"])