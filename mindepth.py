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
		def findnode(node,depth):
			if node.left == None and node.right == None:
				# print node.val,depth
				if self.mindepth == None:
					self.mindepth = depth
				else:
					self.mindepth = min(self.mindepth,depth)
			else:
				# print depth,node.val
				if node.left != None:
					findnode(node.left,depth+1)
				if node.right != None:
					findnode(node.right,depth+1)
		self.mindepth = None
		if root == None:
			return 0
		findnode(root,1)
		return self.mindepth
s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.left.left = TreeNode(5)
print s.minDepth(root)
