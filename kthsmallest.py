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
		self.count = 0
		self.ret = None
		self.dfs(root,k)
		return self.ret
	def dfs(self,node,k):
		if not node:
			return
		self.dfs(node.left,k)
		self.count+=1
		if self.count == k:
			self.ret = node
		self.dfs(node.right,k)




s = Solution()
root = TreeNode(1)
root.right = TreeNode(2)
print s.kthSmallest(root,2).val