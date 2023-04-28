class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = deque()
        queue.append(("0000",0))
        deadends = set(deadends)
        visited = set()
        visited.add("0000")

        while queue:
            string, turn = queue.popleft()

            if string == target:
                return turn
            
            if string in deadends:
                continue

            for i in range(4):
                digit = int(string[i])
                for dire in [-1,1]:
                    new_digit = (digit + dire) % 10

                    n_string = string[:i] + str(new_digit) + string[i+1:]
                    if n_string not in visited:
                        visited.add(n_string)
                        queue.append((n_string, turn + 1))
            
        return -1