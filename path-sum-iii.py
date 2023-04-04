# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = 0
        def backtrack(root,k,path):
            nonlocal count
            if not root:
                return
            path.append(root.val)
            backtrack(root.left,k,path)
            backtrack(root.right,k,path)
            s = 0
            for i in range(len(path)-1,-1,-1):
                s += path[i]
                if s == k:
                    count += 1
            path.pop()
        backtrack(root,targetSum,[])
        return count