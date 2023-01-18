class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # comparator function, compares by changeing the numbers to string
        def compare(x, y):
            num1 = str(x)+str(y)
            num2 = str(y)+str(x)
            if num1 > num2:
                return 1
            else:
                return -1

        # sort nums using the comparator function
        nums.sort(key=functools.cmp_to_key(compare), reverse=True)
        
        # concatenate nums 
        ans = ""
        for num in nums:
            ans += str(num)
        if ans.count("0") == len(ans):
            return "0"
        return ans