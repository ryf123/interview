# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def oddEvenList(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		if head == None:
			return None
		odd_head = head
		even_head = head.next
		odd_current,even_current = odd_head,even_head
		while odd_current and even_current:
			print odd_current.val,even_current.val
			odd_current.next = odd_current.next.next
			odd_current = odd_current.next
			if odd_current:
				even_current.next = even_current.next.next
				even_current = even_current.next
		odd_current.next = even_head
		return head