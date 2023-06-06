# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}

        def solve(root):
            if not root:
                return 0
            
            if root in memo:
                return memo[root]
            cur = root.val
            if root.left:
                cur += solve(root.left.left) + solve(root.left.right)
            if root.right:
                cur += solve(root.right.left) + solve(root.right.right)
            skip_cur = solve(root.left) + solve(root.right)

            memo[root] = max(cur,skip_cur)
            return memo[root]

        return solve(root)