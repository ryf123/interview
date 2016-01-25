# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param {ListNode} head
	# @return {ListNode}
	def deleteDuplicates(self, head):
		current = head
		dummy = ListNode(0)
		dummy.next = head
		prev = dummy
		while(current != None):
			duplicate = False
			while (current and current.next and current.val == current.next.val):
				current.next = current.next.next
				duplicate = True
			if duplicate:
				prev.next = current.next if current else None
			else:
				prev = current
			current = current.next if current else None
		return dummy.next
s = Solution()
head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(2)
print s.deleteDuplicates(head)
