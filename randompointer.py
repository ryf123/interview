# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
	def __init__(self, x):
		self.label = x
		self.next = None
		self.random = None

class Solution(object):
	def copyRandomList(self, head):
		"""
		:type head: RandomListNode
		:rtype: RandomListNode
		"""
		newhead = None
		newprev = None
		current = head
		while(current != None):
			if newhead == None:
				newhead = RandomListNode(current.label)
				newprev = newhead
			else:
				newprev.next = RandomListNode(current.label)
				newprev = newprev.next
			newprev.random = current
			temp  =current.next
			current.next = newprev
			current = temp
		newcurrent = newhead
		prev = None
		while(newcurrent != None):
			if prev != None:
				prev.next = newcurrent.random
			prev = newcurrent.random

			if newcurrent.random.random:
				if newcurrent.random.random.next:
					newcurrent.random = newcurrent.random.random.next
			else:
				newcurrent.random = None

			newcurrent = newcurrent.next
		return newhead
s = Solution()
head = RandomListNode(-1)
#next = RandomListNode(2)
#head.next = next
#head.random = next
#next.random = head
newhead = s.copyRandomList(head)
while newhead:
	print newhead.label,newhead.random.label
	newhead = newhead.next


