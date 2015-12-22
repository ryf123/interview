
# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None
class Solution:
	# @param {ListNode} head
	# @param {integer} k
	# @return {ListNode}
	def rotateRight(self, head, k):
		if k <= 0:
			return head
		current = head
		count = 0 
		while(current != None):
			count+=1
			current = current.next
		if count == 0:
			return None
		k = k%count
		current = head
		for i in xrange(k):
			current = current.next
		p2 = head
		while (current.next != None):
			current = current.next
			p2 = p2.next
		current.next = head
		newhead = p2.next
		p2.next = None
		return newhead
s = Solution()
current = ListNode(0)
head = current
for i in range(1,5):
	current.next = ListNode(i)
	current = current.next
newhead = s.rotateRight(head,2)
count = 0
while(newhead != None):
	print newhead.val
	newhead = newhead.next
	count +=1
	if count == 100:
		break