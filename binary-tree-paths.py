# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.ans = []

        def backtrack(root,path):
            if not root:
                return
            path.append(root.val)
            if not root.left and not root.right:
                self.ans.append("->".join(map(str,path[:])))
            backtrack(root.left,path)
            backtrack(root.right,path)
            path.pop()


        backtrack(root,[])

        return self.ans