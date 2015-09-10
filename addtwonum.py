# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def addTwoNumbers(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		add1 = ""
		add2 = ""
		while l1:
			add1+= str(l1.val)
			l1 = l1.next
		while l2:
			add2+= str(l2.val)
			l2 = l2.next
		add1 = add1[::-1]
		add2 = add2[::-1]
		sumnum = list(str(int(add1) + int(add2)))
		sumnum = sumnum[::-1]
		dummy = ListNode(1)
		current = dummy
		for num in sumnum:
			current.next = ListNode(int(num))
			current = current.next
		return dummy.next
s = Solution()
l1 = ListNode(15)
l2 = ListNode(100)
head = s.addTwoNumbers(l1,l2)
while head:
	print head.val
	head = head.next


