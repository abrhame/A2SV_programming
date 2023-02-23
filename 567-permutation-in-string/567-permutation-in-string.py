class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = Counter(s1)
        window_counter = Counter(s2[:len(s1)])
        
        for i in range(len(s1), len(s2)):
            if s1_counter == window_counter:
                return True
            window_counter[s2[i]] += 1
            window_counter[s2[i-len(s1)]] -= 1
            if window_counter[s2[i-len(s1)]] == 0:
                del window_counter[s2[i-len(s1)]]
        if window_counter == s1_counter:
            return True
        return False