class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque()
        seen = set()
        seen.add(0)
        for room in rooms[0]:
            queue.append(room)
            seen.add(room)
        
        while queue:
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                for n in rooms[node]:
                    if n not in seen:
                        queue.append(n)
                        seen.add(n)
        if len(seen) == len(rooms):
            return True
        return False