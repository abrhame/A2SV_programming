# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque()
        queue.append(root)
        dict = defaultdict(list)
        dict[0].append(root.val)
        i = 0
        while queue:
            n = len(queue)
            i += 1
            for _ in range(n):
                node = queue.popleft()
                if node.left:
                    dict[i].append(node.left.val)
                    queue.append(node.left)
                if node.right:
                    dict[i].append(node.right.val)
                    queue.append(node.right)
        ans = []
        # print(dict)
        for k,v in dict.items():
            av = sum(v)/len(v)
            ans.append(av)
        return ans