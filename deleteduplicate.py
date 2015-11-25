# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None
from collections import Counter
class Solution(object):
	def deleteDuplicates(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		c = Counter()
		current = head
		while current:
			c[current.val] +=1
			current = current.next
		dummy_head = ListNode(1)
		dummy_head.next = head 
		current = head
		prev = dummy_head
		while current:
			if c[current.val] >1:
				current = current.next
				prev.next = current
			else:
				prev = current
				current = current.next
		return dummy_head.next
s = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
print s.deleteDuplicates(head)
