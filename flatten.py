# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param {TreeNode} root
	# @return {void} Do not return anything, modify root in-place instead.
	def flatten(self, root):
		dummyhead = TreeNode(0)
		self.current = dummyhead
		self.converttolist(root)
		return dummyhead.right
	def converttolist(self,node):
		if node != None:
			right = node.right
			left = node.left			
			self.current.right = node
			self.current.left = None
			self.current = node
			self.converttolist(left)
			self.converttolist(right)
t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
s  = Solution() 
s.flatten(t) 

		