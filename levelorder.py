# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
class Solution(object):
	def isSymmetric(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""
		if root == None:
			return True
		else:
			return self.sysmmetric(root.left,root.right)

	def sysmmetric(self,p,q):
		if p == None and q == None:
			return True
		elif p  == None or q == None:
			return False
		else:
			if p.val == q.val:
				return self.sysmmetric(p.left,q.right) and self.sysmmetric(p.right,q.left)
			else:
				return False


n = TreeNode(1)
n.left = TreeNode(3)
n.right = TreeNode(3)
# n = None
s = Solution()
print s.isSymmetric(n)