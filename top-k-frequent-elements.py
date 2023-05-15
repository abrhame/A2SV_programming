class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def quick_sort(arr):
            if len(arr) <= 1:
                return arr
            pivot = len(arr) //2
            left = [x for x in arr if x[0] < arr[pivot][0]]
            equal = [x for x in arr if x[0] == arr[pivot][0]]
            right = [x for x in arr if x[0] > arr[pivot][0]]

            return quick_sort(left) + equal + quick_sort(right)

        def solve(nums):
            count = Counter(nums)
            arr = []
            for e,v in count.items():
                arr.append([v,e])
            
            arr = quick_sort(arr)
            print(arr)
            ans = []

            print(arr[0][1])
            
            end = len(arr) - k
            while end < len(arr):
                ans.append(arr[end][1])
                end += 1
            
            return ans
        return solve(nums)