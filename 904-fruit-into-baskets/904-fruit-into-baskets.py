class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = Counter()
        res = 0
        l = 0
        for i in range(len(fruits)):
            basket[fruits[i]] += 1
            while len(basket) > 2:
                basket[fruits[l]] -= 1
            
                if basket[fruits[l]] == 0:
                    del basket[fruits[l]]
                    
                l += 1
                

            res = max(res, i - l + 1)
        return res