# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def rob(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		return max(self.walk(root))
	def walk(self,node):
		if not node:
			return [0,0]
		right = self.walk(node.right)
		left = self.walk(node.left)
		return [(node.val + right[1] + left[1]),(max(right) + max(left))]
s = Solution()
s.rob(None)

