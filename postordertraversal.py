# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def postorderTraversal(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		if root == None:
			return []
		stack = [root]
		ret = []
		while len(stack):
			node = stack[-1]
			r,l = node.right,node.left
			if not r and not l:
				val = stack.pop().val
				ret.append(val)
			else:
				if r!= None:
					stack.append(r)
				if l!= None:
					stack.append(l)
				node.left,node.right = None,None
		return ret


s = Solution()
root = TreeNode(2)
root.left = TreeNode(1)
root.left.left = TreeNode(4)
root.right = TreeNode(3)
print s.postorderTraversal(root)
