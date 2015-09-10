class Solution(object):
	def levelOrderBottom(self, root):
		"""
		:type root: TreeNode
		:rtype: List[List[int]]
		"""
		if root != None:
			stack = [root]
		else:
			return []
		ret = []
		while(stack):
			tempstack = []
			valstack = []
			while stack:
				n = stack.pop(0)
				valstack.append(n.val)
				if n.left != None:
					tempstack.append(n.left)
				if n.right != None:
					tempstack.append(n.right)
			ret.append(valstack)
			stack = tempstack
		return ret[::-1]