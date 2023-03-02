class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def f(m,string):
            if m == 0:
                return string
            
            string += "1" + "".join(["1" if ch == "0" else "0" for ch in string])[::-1]
            return f(m-1,string)


        s = "0"
        m = n
        ans = f(m,s)
        return ans[k-1]