# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):
        if root == None:
            return None
        if root ==  p:
            return p
        if root == q:
            return q
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        if left != None and right != None:
            return root
        return (left if left != None else right)
        
tn = TreeNode(6)
tn.left = TreeNode(2)
tn.right = TreeNode(8)
s = Solution()
lca = s.lowestCommonAncestor(tn,tn.left,tn.right)
print lca.val