# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self,inorder,postorder):
        """
        :type postorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not len(inorder) or not len(postorder):
            return None
        treeVale = postorder.pop()
        root = TreeNode(treeVale)
        index = inorder.index(treeVale)
        root.right = self.buildTree(inorder[index+1:],postorder)
        root.left = self.buildTree(inorder[:index],postorder)
        
        return root


def printtree(root):
    if root == None:
        return
    printtree(root.left)
    print root.val
    printtree(root.right)
s = Solution()
root = s.buildTree([1,2,3,4,5,6,7],[1,3,2,5,7,6,4])
printtree(root)