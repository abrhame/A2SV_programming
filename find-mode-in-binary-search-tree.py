# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.store = Counter()
    
    def traverse(self,root):
        if not root:
            return
        self.store[root.val] += 1
        self.traverse(root.left)
        self.traverse(root.right)

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.traverse(root)
        value = max(self.store.values())
        ans = []
        for key,val in self.store.items():
            if val == value:
                ans.append(key)
        return ans