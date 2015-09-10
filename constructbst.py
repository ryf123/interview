# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not len(inorder) or not len(preorder):
            return None
        treeVale = preorder.pop(0)
        root = TreeNode(treeVale)
        index = inorder.index(treeVale)
        root.left = self.buildTree(preorder,inorder[:index])
        root.right = self.buildTree(preorder,inorder[index+1:])
        return root


def printtree(root):
    if root == None:
        return
    printtree(root.left)
    print root.val
    printtree(root.right)
s = Solution()
root = s.buildTree([2,1,3],[1,2,3])
printtree(root)