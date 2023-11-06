# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        res = []
        de = set(to_delete)
        def helper(node,is_root):
            if not node: return None

            to_del = node.val in de

            if is_root and not to_del:
                res.append(node)  
            
            node.left = helper(node.left, to_del)
            node.right = helper(node.right, to_del)

            return None if to_del else node

        helper(root, True)

        return res