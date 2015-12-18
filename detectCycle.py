# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
	def detectCycle(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		current = head
		intersection = self.isCycle(head)
		print intersection.val
		if intersection == None:
			return None
		else:
			while current != intersection:
				current = current.next
				intersection = intersection.next
		return current

	def isCycle(self,head):
		if head == None:
			return head
		slow,fast = head,head
		while True:
			if fast == None or fast.next == None:
				return None
			slow = slow.next
			fast = fast.next.next
			if slow == fast:
				break
		return slow
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = head.next
s = Solution()
print s.detectCycle(head)


		
