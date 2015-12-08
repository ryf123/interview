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
		nodelist = []
		node = root
		while node:
			nodelist.append(node)
			node = node.left
		i = 0
		while i<k and len(nodelist):
			node = nodelist.pop()
			i+=1
			right = node.right
			while right:
				nodelist.append(right)
				right = right.left
			if i==k:
				return node.val
		return None




s = Solution()
root = TreeNode(1)
root.right = TreeNode(2)
print s.kthSmallest(root,2).val