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
		
		current = head
		prehead = None
		newhead = None
		dummy = head
		l = 0
		while dummy:
			l+=1
			dummy = dummy.next
		if l == 0:
			return None
		# k = k%l
		i = 0
		while current!= None:

			stack.append(current)
			tempnext = current.next
			
			i+=1
			# print current.val,i,k
			if i== k:
				stack = stack[::-1]
				for j,node in enumerate(stack):
					if j!= k-1:
						node.next = stack[j+1]
				if prehead != None:
					prehead.next = stack[0]
				else:
					newhead = stack[0]
				prehead = stack[-1]
				prehead.next = tempnext
				stack = []
				i = 0
			current = tempnext
		# current.next = None
		return newhead if newhead!= None else head
s = Solution()
# h = ListNode(1)
h = None
# c = h
for x in range(1,6):
	if h == None:
		h = ListNode(x)
		c = h
	else:
		c.next = ListNode(x)
		c = c.next
	print c.val
print "========="
h = s.reverseKGroup(h,5)
while h:
	print h.val
	h = h.next
