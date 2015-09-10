# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def removeNthFromEnd(self, head, n):
		"""
		:type head: ListNode
		:type n: int
		:rtype: ListNode
		"""
		stack = []
		current = head
		l = 0
		while current:
			stack.append(current)
			current = current.next
			l+=1
		stack.append(None)
		if n >= l:
			return head.next
		else:
			stack[l-n-1].next = stack[l-n+1]
			return head
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
s = Solution()
head = s.removeNthFromEnd(head,1)
while head:
	print head.val
	head = head.next