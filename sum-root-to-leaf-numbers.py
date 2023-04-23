# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def solve(root,arr):
            nonlocal ans
            if not root:
                return

            
            arr.append(str(root.val))
            if root and not root.left and not root.right:
                # print(arr)
                # print(root.val)
                ans += int("".join(arr))
            solve(root.left,arr)
            solve(root.right,arr)
            arr.pop()
        
        solve(root,[])
        return ans