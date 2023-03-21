# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        store = defaultdict(list)
        
        def helper(root,y,x):
            if not root:
                return 
            store[x].append([y,root.val])
            helper(root.left, y + 1, x - 1)
            helper(root.right, y + 1, x + 1)

        helper(root,0,0)
        print(store)
        output = []

        for key in sorted(store.keys()):
            column = sorted(store[key])
            column_output = [val[1] for val in column]
            output.append(column_output)
        return output