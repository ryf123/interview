class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
class Solution:
	# @param {TreeNode} root
	# @return {integer[]}
	def rightSideView(self, root):
		def bst(stack):
			ret = []
			while len(stack) >0:
				node = stack.pop(0)
				if len(stack) == 0:
					self.rightnode.append(node.val)
				if node.left != None:
					ret.append(node.left)
				if node.right != None:
					ret.append(node.right)
			if len(ret) !=0:
				bst(ret)
			return 
		self.rightnode = []
		bst(root)
		return self.rightnode
s  = Solution()
root = TreeNode(1)
root.right = TreeNode(3)
root.left = TreeNode(2)
root.right.right = TreeNode(5)
print s.rightSideView([root])