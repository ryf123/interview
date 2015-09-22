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
		stack = [root]
		while len(stack):
			tempstack = []
			prev = None
			# print stack
			while len(stack):
				
				node = stack.pop(0)
				# print node.val
				if node:
					if node.left:
						tempstack.append(node.left)
					if node.right:
						tempstack.append(node.right)
				if prev != None:
					prev.next = node
				prev = node
			stack = tempstack
s = Solution()
head = TreeLinkNode(1)
head.left = TreeLinkNode(2)
head.right = TreeLinkNode(3)
s.connect(head)
print head.left.next.val
