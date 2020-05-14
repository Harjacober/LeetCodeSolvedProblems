"""
**Explanation:**  Let's start from the first level of the binary tree `root` and
the first element in the array `arr[i] where i=0`. if the value at the root node
`root.val != arr[i]`, we immediately `return False`. 
But if the value at the root node `root.val == arr[0]` is equal to the element at
the `arr[i]`, there are two conditions two handle:
**(1)** if we have completely moved through the array, i.e `i==len(arr)`, and we
are at the leaf node i.e `node.right and node.left` are `None`, we  `return True
` . Else we `return False`(as valid subsequence path must always terminate at a leaf node).
**(2)** if we have not moved through the array completely yet i.e. `i<len(arr)`
and the current node still has at least one child, we move one level below the
tree and also increment `i` i.e `i+=1`  by visiting the left child `dfs(node.left, i)` and right child `dfs(node.right,i)`.
We return true if either the left or right child is `True` i.e. `return dfs(node.left, i) or dfs(node.right,i)`.
```
"""
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        def dfs(node,i):
            if node and node.val==arr[i]:
                i += 1
                if i==len(arr):
                    return not (node.left or node.right)
                else:
                    return dfs(node.left,i) or dfs(node.right,i)
            else:
                return False
            
                
        if root:return dfs(root,0)
        else: return False
```
