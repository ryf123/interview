# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def sumNumbers(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		def findpath(path,node):
			if node == None:
				return
			if node.left == None and node.right == None:
				return self.ret.append(path+[node.val])
			path.append(node.val)
			findpath(path,node.left)
			findpath(path,node.right)
			path.pop()
		self.ret = []
		findpath([],root)
		total = 0
		for r in self.ret:
			r = map(str,r)
			total += int("".join(r))
		return total
s = Solution()
root = TreeNode(4)
#root.left = TreeNode(2)
#root.right = TreeNode(6) 
print s.sumNumbers(root)