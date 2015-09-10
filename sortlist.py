class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def sortList(self, head):
        def compare(n1,n2):
            return -1 if n1.val < n2.val else 1
        if head == None:
            return None
        current =  head
        nodelist = []
        while(current != None):
            nodelist.append(current)
            current = current.next
        nodelist = sorted(nodelist,cmp=compare)
        head = nodelist[0]
        current = head
        prev= None
        for node in nodelist:
            current = node
            if prev != None:
                prev.next = current
            prev = current
        prev.next = None
        return head
s = Solution()
head = ListNode(2)
head.next = ListNode(1)
ret = s.sortList(head)
while ret != None:
    print ret.val
    ret = ret.next
