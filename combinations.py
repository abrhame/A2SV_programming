class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []

        def backtrack(idx,combination):

            if len(combination) == k:
                combinations.append(combination[:])
                return
            # if 
            #     return
            for i in range(idx,n + 1):
                    combination.append(i)
                    backtrack(i+1,combination)
                    combination.pop()



        backtrack(1,[])
        return combinations