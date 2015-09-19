class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if head == None:
            return 0
        headval = head.val
        headnext = head.next
        current = head
        while(1):
            if current.next == None:
                return 0
            else:
                current = current.next
                if current.val == headval && current.next == headnext:
                    return 1