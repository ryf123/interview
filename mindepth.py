class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
class Solution(object):
	def minDepth(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		if root == None:
			return 0
		stack = [[root,1]]
		while stack:
			[node,height] = stack.pop(0)
			if node.left == None and node.right == None:
				return height
			if node.left:
				stack.append([node.left,height+1])
			if node.right:
				stack.append([node.right,height+1])
s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.left.left = TreeNode(5)
print s.minDepth(root)
