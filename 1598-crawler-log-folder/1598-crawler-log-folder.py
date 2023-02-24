class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        for log in logs:
            if "../" in log and count > 0:
                count -= 1
            elif "./" in log or ("../" in log and count == 0):
                continue
            else:
                count += 1
        return count