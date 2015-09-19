#Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param {ListNode[]} lists
	# @return {ListNode}
	def mergeKLists(self, lists):
		head1 = None
		head2 = None
		l = len(lists)
		if l == 1:
			return lists[0]
		k = 0
		for i,mylist in enumerate(lists):
			if mylist == None:
				continue
			if head1 == None:
				head1 = mylist
				k +=1
				continue
			head2 = mylist

			c1 = head1
			c2 = head2
			j = 0
			while(c1 != None or c2 != None):
				#print c1.val
				if c2 != None and c1 != None:
					if c2.val > c1.val:
						current = c1 
						c1 = c1.next
					else:
						current = c2
						c2 = c2.next
				elif c2 == None and c1 != None:
					current = c1
					c1 = c1.next
				else:
					current = c2
					c2 = c2.next
				if j==0:
					head1 = current
					prev = current
				else:
					prev.next = current
					prev = current  
				j +=1
			k+=1
		return head1
s = Solution()
head1 = ListNode(-1)
head1.next = ListNode(1)
head2 = ListNode(-3)
head2.next = ListNode(1)
head3 = ListNode(-2)

lists = [head1,head2,head3]
head = s.mergeKLists(lists)
while(head!= None):
	print head.val
	head = head.next



