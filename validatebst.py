# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param {TreeNode} root
	# @return {boolean}
	def isValidBST(self, root):
		def inorder(root):
			ret = []
			if root == None:
				return ret
			ret += inorder(root.left)
			ret.append(root.val)
			ret += inorder(root.right)
			return ret
		inordertree = inorder(root)
		print inordertree
		l = len(inordertree)
		for i,nodeval in enumerate(inordertree):
			if i == l-1:
				continue
			if nodeval >= inordertree[i+1]:
				return False
		return True
s =Solution()
root = TreeNode(1)
root.left = TreeNode(1)
#root.right = TreeNode(3)
print s.isValidBST(root)