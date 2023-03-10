# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        count = 0
        if not root:
            return 0
        def helper(root):
            nonlocal count
           
            if not root.left and not root.right:
                count += 1
                return [root.val, 1]
            
            elif not root.left:
                right = helper(root.right)
                left = [0, 0]
            
            elif not root.right:
                left = helper(root.left)
                right = [0, 0]
            else:
                left = helper(root.left)
                right = helper(root.right)
            summ = (left[0] + right[0] + root.val)
            num_nodes = left[1] + right[1] + 1
            average = summ // num_nodes

            if root.val == average:
                count += 1
            
            return [summ,num_nodes]

        helper(root)
        return count