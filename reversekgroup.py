# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def reverseKGroup(self, head, k):
		"""
		:type head: ListNode
		:type k: int
		:rtype: ListNode
		"""
		stack = []
		reversestack = []
		current = head

		if k == 0:
			return head
		while current:
			stack.append(current)
			current = current.next
		if k> len(stack):
			return head
		i = 0

		for i in xrange(len(stack)/k):
			reversestack += stack[k*i:(i+1)*k][::-1]

		reversestack += stack[(i+1)*k:]
		newhead = reversestack[0]
		current = newhead
		for node in reversestack[1:]:
			current.next = node
			current = node
		reversestack[-1].next = None
		return newhead

s = Solution()
# h = ListNode(1)

for k in xrange(7):
	head = None
	# c = h
	for x in range(1,6):
		if head == None:
			head = ListNode(x)
			c = head
		else:
			c.next = ListNode(x)
			c = c.next
	
	h = head
	h = s.reverseKGroup(head,k)
	print "========="
	while h:
		print h.val
		h = h.next
	print "========="
