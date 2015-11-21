# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param {ListNode} head
	# @return {ListNode}
	def swapPairs(self, head):
		dummyhead = ListNode(0)
		dummyhead.next = head
		prev = dummyhead
		current = head
		count = 0
		if current == None:
			return None
		while (current.next != None):
			count +=1
			prev.next = current.next
			next = current.next.next
			current.next.next = current
			prev = current
			current.next = next
			current = next
			if current == None:
				break
		return dummyhead.next

s = Solution()
temp = ListNode(0)
current = ListNode(0)
temp.next = current
head = temp
for i in range(0,5):
	current.next = ListNode(i)
	current = current.next
newhead = s.swapPairs(head)
count = 0
while(newhead != None):
	print newhead.val
	newhead = newhead.next
	count +=1
	if count == 100:
		break