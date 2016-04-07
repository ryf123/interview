# Definition for binary tree with next pointer.
class TreeLinkNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		self.next = None

class Solution(object):
	def connect(self, root):
		"""
		:type root: TreeLinkNode
		:rtype: nothing
		"""
		head = root
		while head != None:
			dummyCurrent = TreeLinkNode(0)
			current = dummyCurrent
			while head != None:
				if head.left != None:
					current.next = head.left
					current = current.next
				if head.right != None:
					current.next = head.right
					current = current.next
				head = head.next
			head = dummyCurrent.next
s = Solution()
head = TreeLinkNode(1)
head.left = TreeLinkNode(2)
head.right = TreeLinkNode(3)
s.connect(head)
print head.left.next.val
