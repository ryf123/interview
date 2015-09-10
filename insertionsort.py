# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def insertionSortList(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		current = head
		newhead = None
		i = 0
		while current:
			newcurrent = newhead
			newprev = None
			next = current.next
			if newhead == None:
				newhead = current
				newhead.next = None
				current = next
				# print current.val,newhead.val
				i+=1
				continue
			j = 0
			# print "---"
			
			while j < i:
				# print current.val,newcurrent.val,[j,i],newhead.val
				if newprev == None:
					# print "newprev == None"
					# insert to beginning
					if current.val < newcurrent.val:
						newhead = current
						newhead.next = newcurrent
						break
					newprev = newcurrent
					newcurrent = newcurrent.next
				else: 
					#insert to middle
					# print "else"
					if current.val < newcurrent.val:
						# print newprev.val,current.val
						current.next = newprev.next
						newprev.next = current
						break
					else:
						newprev = newcurrent
						newcurrent = newcurrent.next
						# print newcurrent.val
				j+=1
			# insert to the end
			# print [j,i]
			if i == j and newprev:
				newprev.next = current
				current.next = None

			i+=1
			current = next
			# print "======"
		return newhead
s = Solution()
head = ListNode(10)
head.next = ListNode(2)
head.next.next = ListNode(15)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(100)
# 10->2->3
# 10->2->3
# 2->10->2
newhead =  s.insertionSortList(head)
while (newhead != None):
	print newhead.val
	newhead = newhead.next
	# break

