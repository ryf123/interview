class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
	# @param {TreeNode} root
	# @return {boolean}
	def isValidBST(self, root):
		self.prev= None
		return self.traversal(root)
	def traversal(self,node):
		if node == None:
			return True
		if not self.traversal(node.left):
			return False
		if self.prev:
			if node.val < self.prev.val:
				return False
		self.prev = node
		return self.traversal(node.right)
s = Solution()
head = TreeNode(1)
head.left = TreeNode(0)
print s.isValidBST(head)