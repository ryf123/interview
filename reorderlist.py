# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {void} Do not return anything, modify head in-place instead.
    def reorderList(self, head):
        c = head
        if c == None:
            return
        stack = []
        l = 0
        current = head

        while(c != None):
            stack.append(c)
            c = c.next
            l+=1
        while (current != None):
            # print current.val
            current = current.next

        # print stack[l-1].val

        current = head
        prev = None
        for i in range(0,l/2):
            if i < l-i-1:
                start = stack[i]
                end = stack[l-i-1]
                if prev != None:
                    prev.next = start
                start.next = end
                prev = end
            # if i!=0:
            #     current.next = a[i]
            #     current = current.next
            # if i<= l/2:
            #     current.next = a[l-i-1]
            #     current =current.next
        if prev != None:
            if l%2:
                prev.next = stack[l/2]
                prev = prev.next
            prev.next = None
head = ListNode(-1)
current = head
for x in xrange(3):
    # print x
    current.next = ListNode(x)
    current = current.next
current = head

s = Solution()
s.reorderList(head)
current = head
while (current != None):
    print current.val
    current = current.next
        