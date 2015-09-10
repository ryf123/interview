# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
	def binaryTreePaths(self, root):
		"""
		:type root: TreeNode
		:rtype: List[str]
		"""
		def walk(node,path):
			if node.left == None and node.right == None:
				self.ret.append(path+[str(node.val)])
			if node.left  != None:
				walk(node.left,path+[str(node.val)])
			if node.right != None:
				walk(node.right,path+[str(node.val)])
			return
		if root == None:
			return []
		self.ret = []
		walk(root,[])
		retlist = []
		for r in self.ret:
			retlist.append("->".join(r))
		return retlist
s = Solution()
root = TreeNode(1)
root.right  = TreeNode(2)
root.right.right = TreeNode(5)
root.right.left = TreeNode(6)
root.left = TreeNode(3)
print s.binaryTreePaths(root)