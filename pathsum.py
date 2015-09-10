# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {integer[][]}
    def pathSum(self, node, total):
        def path(root,sum,currentpath):
            if root == None:
                return 
            currentpath.append(root.val)
            if sum-root.val == 0 and root.left==None and root.right==None:
                sol.append(currentpath)
                return 
            ret1 = path(root.left,sum-root.val,currentpath[:]) 
            ret2 =  path(root.right,sum-root.val,currentpath[:])
            currentpath.pop(0)
            return 
        sol = []
        path(node,total,[])
        return sol
s = Solution()
root = TreeNode(0)
root.right = TreeNode(1)
root.left = TreeNode(1)
print s.pathSum(root,1)