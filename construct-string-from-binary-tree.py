# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        string = ""
        def dfs(root):
            if not root:
                return ""
            string = str(root.val)
            if not root.left and not root.right:
                return string
            
            string += "(" + dfs(root.left) + ")"
            if root.right:
                string += "(" + dfs(root.right) + ")"

            return string

        return dfs(root)