class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        ans=[-2147483648]
        def helper(node,ans):
            if not node: return ans[0]
            left=helper(node.left,ans)
            right=helper(node.right,ans)
            ans.append(left)
            ans.append(right)
            if left==ans[0]: left=0
            if right==ans[0]:
                right=0
            best = max(node.val+max(left,right),node.val)
            ans.append(best)
            ans.append(node.val)
            ans.append(left+right+node.val)
           
            return best
        helper(root,ans)
        return max(ans)
