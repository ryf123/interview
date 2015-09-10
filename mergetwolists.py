# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
	def mergeTwoLists(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		c1 = l1
		c2 = l2
		# newhead = None
		dummy = ListNode(1)
		current = dummy
		while(c1 != None and c2 != None):
			if c1.val <= c2.val:
				current.next = c1
				c1 = c1.next
			else:
				current.next = c2
				c2 = c2.next
			current = current.next
		if c1 == None and c2 != None:
			current.next = c2
		else:
			current.next = c1
		return dummy.next
s = Solution()
l1 = None
l2 = ListNode(2)
l2.next = ListNode(4)
l2.next.next = ListNode(6)
head = s.mergeTwoLists(l1,l2)
while (head):
	print head.val
	head = head.next