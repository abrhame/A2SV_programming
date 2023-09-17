class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0, 1)]) 
        visited = set([(0, 1)])
        steps = 0

        while queue:
            size = len(queue)
            for _ in range(size):
                position, speed = queue.popleft()

                if position == target:
                    return steps

                new_position = position + speed
                new_speed = speed * 2
                if (new_position, new_speed) not in visited and abs(new_position - target) < target:
                    queue.append((new_position, new_speed))
                    visited.add((new_position, new_speed))

                new_speed = -1 if speed > 0 else 1
                if (position, new_speed) not in visited and abs(position - target) < target:
                    queue.append((position, new_speed))
                    visited.add((position, new_speed))

            steps += 1

        return -1