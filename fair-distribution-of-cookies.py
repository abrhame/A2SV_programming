class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        cookies.sort(reverse=True)
        ans = +float("inf")
        bag = [0] * k

        def backtrack(idx,child):
            nonlocal ans
            nonlocal bag
            if idx >= len(cookies):
                ans = min(ans,max(bag))
                return
            if max(bag) >= ans:
                return
            for i in range(k):
                    bag[i] += cookies[idx]
                    backtrack(idx + 1,child)
                    bag[i] -= cookies[idx]
        backtrack(0,[])

        return ans