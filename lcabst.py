# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def lowestCommonAncestor(self, root, p, q):
		"""
		:type root: TreeNode
		:type p: TreeNode
		:type q: TreeNode
		:rtype: TreeNode
		"""
		if p == None or q == None:
			return None

		if root== None:
			return None
		if root.val >= min(p.val,q.val) and root.val <= max(p.val,q.val):
			return root
		left = self.lowestCommonAncestor(root.left,p,q)
		right = self.lowestCommonAncestor(root.right,p,q)
		return left if left else right
root = TreeNode(1)
root.right = TreeNode(2)
s = Solution()
print s.lowestCommonAncestor(root,root,root.right).val