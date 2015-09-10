# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def isBalanced(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""
		# self.balance
		if root == None:
			return True
		lh,lbalanced = self.balance(root.left)
		rh,rbalanced = self.balance(root.right)
		# print lh,rh
		if lbalanced and rbalanced and abs(lh-rh) <=1:
			return True
		else:
			return False
	def balance(self,node):
		if node == None:
			return 0,True
		else:
			lh,lbalanced = self.balance(node.left)
			rh,rbalanced = self.balance(node.right)
			# print [lh,rh],node.val
		if lbalanced and rbalanced and abs(lh-rh) <=1:
			return max(lh,rh)+1,True
		else:
			return 0,False
s = Solution()
h = TreeNode(1)
h.left = TreeNode(2)
h.left.left = TreeNode(3)
h.left.left.left = TreeNode(4)
h.right = TreeNode(20)
h.right.right = TreeNode(30)
h.right.right.right = TreeNode(40)
print s.isBalanced(h)