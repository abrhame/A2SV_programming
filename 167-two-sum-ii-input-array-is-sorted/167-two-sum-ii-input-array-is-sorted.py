class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         left = 0
#         right = len(numbers) - 1
        
#         while left < right:
#             if numbers[left] + numbers[right] == target:
#                 return [left + 1, right + 1]
#             elif numbers[left] + numbers[right] < target:
#                 left += 1
#             else:
#                 right -= 1

# *** Method 2 ***
            comp = set()
            for i in range(len(numbers)):
                diff = target - numbers[i]
                if diff in comp:
                    ind = numbers.index(diff)
                    return [ind+1,i+1]
                else:
                    comp.add(numbers[i])
            
        #*** Method 3 ****
        
            #         # comp = set()
            # for i in range(len(numbers)):
            #     diff = target - numbers[i]
            #     if diff in comp:
            #         ind = numbers.index(diff)
            #         return [ind+1,i+1]
            #     else:
            #         comp.add(numbers[i])
            
            
    