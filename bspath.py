# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root the root of the binary tree
    # @return {List[str]} all root-to-leaf paths
    def binaryTreePaths(self, root):
        # Write your code here
        self.ret = []
        self.dfs(root,[])
        return self.ret
    def dfs(self,node,path):
        if node == None:
            return
        path.append(str(node.val))
        if node.left != None:
            self.dfs(node.left,path)
        if node.right != None:
            self.dfs(node.right,path)
        if node.left == None and node.right == None:
            self.ret.append("->".join(path))
        path.pop()
s = Solution()
root = TreeNode(1)
root.right  = TreeNode(2)
root.right.right = TreeNode(5)
root.right.left = TreeNode(6)
root.left = TreeNode(3)
print s.binaryTreePaths(root)