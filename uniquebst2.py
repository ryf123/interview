# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def generateTrees(self, n):
		"""
		:type n: int
		:rtype: List[TreeNode]
		"""
		def buildbst(start,end):
			if start > end:
				return [None]
			ret = []
			for i in range(start,end+1):
				lefts = buildbst(start,i-1)
				rights = buildbst(i+1,end)
				for left in lefts:
					for right in rights:
						node = TreeNode(i)
						node.left = left
						node.right = right
						ret.append(node)
			return ret
		ret = buildbst(1,n)
		return ret
def printtree(root):
	if root == None:
		return
	else:
		print root.val
		print "#"
		printtree(root.left)
		printtree(root.right)
s = Solution()
ret = s.generateTrees(3)
for r in ret:
	print "++++"
	printtree(r)