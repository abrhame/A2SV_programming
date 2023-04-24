"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        def solve(root,d):
            if not root.children:
                return d
            
            max_d = 0
            for child in root.children:
                max_d = max(solve(child,d+1),max_d)
            return max_d
        
        return solve(root,1)