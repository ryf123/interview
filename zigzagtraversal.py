# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def zigzagLevelOrder(self, root):
		"""
		:type root: TreeNode
		:rtype: List[List[int]]
		"""
		if root == None:
			return []
		ret = []
		stack = [root]
		reverse= False
		while(len(stack)):
			temp = []
			tempret = []
			stack = stack[::-1]
			l = len(stack)
			for i in range(0,l):
				node = stack[i]
				if not reverse:
					if node.left != None:
						temp.append(node.left)
					if node.right != None:
						temp.append(node.right)
				else:
					if node.right != None:
						temp.append(node.right)
					if node.left != None:
						temp.append(node.left)
					
				tempret.append(node.val)
			stack = temp
			ret.append(tempret)
			reverse = False if reverse else True
		return ret
s = Solution()
root = TreeNode(2)
root.left = TreeNode(1)
root.left.left = TreeNode(4)
root.right = TreeNode(3)
root.right.right = TreeNode(5)
print s.zigzagLevelOrder(root) 