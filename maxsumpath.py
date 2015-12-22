import sys
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
		self.maxpath = -sys.maxint
		self.solve(0,root)
		return self.maxpath
	def solve(self,total,node):
		if node == None:
			return 0
		leftpath = self.solve(total,node.left)
		rightpath = self.solve(total,node.right)
		self.maxpath = max([leftpath+node.val,rightpath+node.val,leftpath+rightpath+node.val,self.maxpath])
		return max([leftpath+node.val,rightpath+node.val,0])

s = Solution()
head = TreeNode(-1)
head.left = TreeNode(-2)
head.right = TreeNode(-3)
head.right.right = TreeNode(10)
print s.maxPathSum(head)
