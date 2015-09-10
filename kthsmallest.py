class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param {TreeNode} root
	# @param {integer} k
	# @return {integer}
	def kthSmallest(self, root, k):
		def inorder(node):
			nodelist = []
			if node == None:
				return []
			nodelist +=inorder(node.left)
			nodelist.append(node)
			nodelist +=inorder(node.right)
			return nodelist
		inorderlist = inorder(root)
		ret =  inorderlist[k-1]
		return ret.val

s = Solution()
root = TreeNode(1)
# root.right = TreeNode(2)
print s.kthSmallest(root,1)