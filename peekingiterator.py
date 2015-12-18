class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.peekstack = []
        self.iterator = iterator        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if len(self.peekstack) == 0:
            self.peekstack.append(self.iterator.next())
        return self.peekstack[0]

    def next(self):
        """
        :rtype: int
        """
        if len(self.peekstack) >0:
            ret = self.peekstack.pop()
        else:
            ret = self.iterator.next()
        return ret         

    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self.peekstack) >0:
            return True
        else:
            return True if self.iterator.hasNext() else False
nums = iter("abcd")
iter = PeekingIterator(nums)
while iter.hasNext():
    val = iter.peek()   # Get the next element but not advance the iterator.
    print val
    print iter.next()         # Should return the same value as [val]. 
