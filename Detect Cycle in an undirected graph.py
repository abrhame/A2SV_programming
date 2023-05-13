from typing import List
from collections import deque
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
	    visited = set()
	    queue = deque()
	    
	    for i in range(V):
	        if i not in visited:
	            visited.add(i)
	            queue.append((i,-1))
	        while queue:
	            cur,parent = queue.popleft()
	            for k in adj[cur]:
	                if k not in visited:
	                    visited.add(k)
	                    queue.append((k,cur))
	                elif parent != k:
	                    return True
	    return False
	            