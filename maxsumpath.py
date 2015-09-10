# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
	# @param {TreeNode} root
	# @return {integer}
	def maxPathSum(self, root):
		def findmax(node):
			total = 0
			if node == None:
				return 0
			leftsum = max(findmax(node.left),0)
			rightsum = max(findmax(node.right),0)
			total = node.val +leftsum +rightsum 
			if total > self.maxsum:
				self.maxsum = total
			return max(node.val +leftsum,node.val + rightsum)
		if root == None:
			return 0
		self.maxsum = root.val
		findmax(root)
		return self.maxsum 
s = Solution()
head = TreeNode(1)
head.left = TreeNode(-2)
head.right = TreeNode(3)
print s.maxPathSum(head)
