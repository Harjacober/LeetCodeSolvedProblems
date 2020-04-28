class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bstFromPreorder(self, preorder) -> TreeNode:
        def helper(node, val):
            if val < node.val:
                if not node.left: node.left = TreeNode(val)
                else: helper(node.left,val)
            else:
                if not node.right: node.right = TreeNode(val)
                else: helper(node.right,val)
            return

        root = None
        for val in preorder:
            if not root: root = TreeNode(val)
            else: helper(root, val)

        return root

def preOrder(root):
    if root:
        print(root.val)
        preOrder(root.left)
        preOrder(root.right)

a = [8,5,4,3,2,1,7,9,10,12,11,19,18,17,21]

preOrder(Solution().bstFromPreorder(a))
