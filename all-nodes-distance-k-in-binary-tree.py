# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        def solve(root):
            if not root: return
            if root.left:
                graph[root.val].append(root.left.val)
                graph[root.left.val].append(root.val)
                solve(root.left)
            if root.right:
                graph[root.val].append(root.right.val)
                graph[root.right.val].append(root.val)
                solve(root.right)
        solve(root)
        print(graph)
        queue = deque()
        visited = set()
        queue.append(target.val)
        visited.add(target.val)
        level = 0
        ans = []
        if k == 0:
            return[ target.val]
        while queue:
            n = len(queue)
            level += 1
            # print(queue)
            for _ in range(n):
                node = queue.popleft()
                if node not in graph:
                    return ans
                for elem in graph[node]:
                    if elem not in visited:
                        if level == k:
                            ans.append(elem)
                        queue.append(elem)
                        visited.add(elem)
            if level == k:
                return ans

        return ans