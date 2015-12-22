# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def getIntersectionNode(self, headA, headB):
		"""
		:type head1, head1: ListNode
		:rtype: ListNode
		"""
		currentA,currentB = headA,headB
		la,lb = 0,0
		while currentA:
			currentA = currentA.next
			la+=1
		while currentB:
			currentB = currentB.next
			lb+=1
		p1,p2 = 0,0
		currentA,currentB = headA,headB
		if la>lb:
			while p1<la-lb:
				p1+=1
				currentA = currentA.next
		else:
			while p2<lb-la:
				p2+=1
				currentB = currentB.next
		while currentA != None and currentB != None:
			if currentA == currentB:
				return currentA
			currentA = currentA.next
			currentB = currentB.next
		return None
s = Solution()
headA = ListNode(1)
headB = ListNode(0)
headB.next = headA
node =  s.getIntersectionNode(headA,headB)
print node.val