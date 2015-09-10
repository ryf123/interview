# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def inorderTraversal(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		if root == None:
			return []
		stack = [root]
		ret = []
		while (len(stack) >0):
			node = stack.pop()
			if node.left == None and node.right == None:
				ret.append(node)
				continue
			if node.right != None:
				stack.append(node.right)
				node.right = None
			stack.append(node)
			if node.left != None:
				stack.append(node.left)
				node.left = None
		return [r.val for r in ret]
s = Solution()
root = TreeNode(2)
root.left = TreeNode(1)
root.left.left = TreeNode(4)
root.right = TreeNode(3)
print s.inorderTraversal(root)
