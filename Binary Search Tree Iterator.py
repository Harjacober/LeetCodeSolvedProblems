# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = [root]
        self.iter = self.iterator() 

    def iterator(self) -> int: 
        while self.stack:
            while self.stack[-1].left: 
                self.stack.append(self.stack[-1].left)
            node = self.stack.pop()
            if node.right:
                self.stack.append(node.right)  
            else:
                if self.stack:
                    self.stack[-1].left=None
            yield node.val
            
    def next(self) -> int:
        """
        @return the next smallest number
        """ 
        return next(self.iter)
    
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.stack and self.stack[-1]
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
