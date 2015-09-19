# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param {ListNode} head
	# @return {ListNode}
	def swapPairs(self, head):
		if(head == None):
			print "head is None"
			return None
		if head.next == None:
			print "head next is None"
			return head
		if head.next.next == None:
			temp = head
			head = head.next
			head.next = temp
			head.next.next = None
			print "two values"
			return head
		current = head
		prev = None
		pp = None
		pair = 0 # if pair is 1, then swap, else do nothing
		while(current.next != None):
			if current == head:
				# swap the two nodes
				head = current.next # head is 1
				tempnext = current.next.next 
				current.next.next = current # connect 1 to 0
				current.next = tempnext # break connection from 0 to 1, connect 0 to 2
				prev = current # prev is 0
				current = tempnext # current is 2
				print "first time"
				print (head.val,prev.val,current.val)
			else:
				prev.next = current.next
				temp = current.next.next
				current.next.next = current
				current.next = temp

				prev = current
				current = temp # current moves two steps foward
			if current == None:
				break
		return head
s = Solution()
temp = ListNode(0)
current = ListNode(0)
temp.next = current
head = temp
for i in range(0,1):
	current.next = ListNode(i)
	current = current.next
newhead = s.swapPairs(head)
while(newhead != None):
	print newhead.val
	newhead = newhead.next