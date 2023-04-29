# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def solve(root, grandparent, parent):
            if not root:
                return 0
            
            left = solve(root.left, parent, root)
            right = solve(root.right, parent, root)

            if grandparent and grandparent.val % 2 == 0:
                return left + right + root.val
            
            return left + right

        return solve(root, None, None)