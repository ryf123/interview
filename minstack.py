class MinStack(object):

    def __init__(self):
        # do some intialize if necessary
        self.minstack = []
        self.stack = []

    def push(self, number):
        # write yout code here
        self.stack.append(number)
        currentmin = number if len(self.minstack) == 0 else min(self.minstack[-1],number)
        self.minstack.append(currentmin)
    def pop(self):
        # pop and return the top item in stack
        if len(stack) > 0:
	        self.minstack.pop()
	        return self.stack.pop()
    def min(self):
        # return the minimum number in stack
        if len(stack)>0:
        	return self.minstack[-1]