class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.stack = []
        self.buildtree(root)
        
    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
       l = len(self.stack)
       if l > 0:
           return True
       else:
           return False
    # @return an integer, the next smallest number
    def next(self):
        l = len(self.stack)
        if l > 0:
            node = self.stack.pop()
            val = node.val
            if node.right != None:
                node = node.right
                while node:
                    self.stack.append(node)
                    node = node.left
            return val
    def buildtree(self,node):
        while node:
            self.stack.append(node)
            node = node.left
head = TreeNode(2)
head.left = TreeNode(1)
head.right = TreeNode(3)
bsti  = BSTIterator(head)
while bsti.hasNext():
    print bsti.next()