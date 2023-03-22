# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        store = defaultdict(list)

        def traverse(root,level,column):
            if not root:
                return 
            store[level].append(column)
            traverse(root.left,level + 1, column * 2)
            traverse(root.right,level + 1, column * 2 + 1)

        traverse(root,0,0)

        max_width = 0
        for key,val in store.items():
            width = val[-1] - val[0]
            max_width = max(max_width,width + 1)
        print(store)
        return max_width