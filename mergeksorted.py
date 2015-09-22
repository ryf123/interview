#Definition for singly-linked list.
import heapq
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param {ListNode[]} lists
	# @return {ListNode}
	def mergeKLists(self, lists):
		minstack = []
		if not len(lists):
			return None
		for l in lists:
			if l != None:
				heapq.heappush(minstack,(l.val,l))
		newhead = None
		current = newhead
		while len(minstack):
			node = heapq.heappop(minstack)[1]
			if newhead == None:
				newhead = node
				current = newhead
			else:
				current.next = node
				current = node
			if node.next != None:
				heapq.heappush(minstack,(node.next.val,node.next))
		return newhead
s = Solution()
head1 = ListNode(-1)
head1.next = ListNode(1)
head2 = ListNode(-3)
head2.next = ListNode(1)
head3 = ListNode(-2)

lists = [head1,head2,head3]
lists = [None]
head = s.mergeKLists(lists)
while(head!= None):
	print head.val
	head = head.next



