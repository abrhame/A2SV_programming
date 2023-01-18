class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x, y):
            num1 = str(x)+str(y)
            num2 = str(y)+str(x)
            if num1 > num2:
                return 1
            else:
                return -1

    # Calling
        nums.sort(key=functools.cmp_to_key(compare), reverse=True)
        ans = ""
        for num in nums:
            ans += str(num)
        if ans.count("0") == len(ans):
            return "0"
        return ans