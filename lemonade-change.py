class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool: 
        change = {5:0,10:0,20:0}
        for i,val in enumerate(bills):
            if val == 5:
                change[5] += 1
            elif val == 10:
                change[10] += 1
                if change[5] == 0: 
                    return False
                change[5] -= 1
            elif val == 20:
                change[20] += 1
                if (change[10] == 0 and change[5] < 3) or change[5] == 0:
                    return False
                if change[10] == 0 and change[5] >= 3:
                    change[5] -= 3
                else:
                    change[10] -= 1
                    change[5] -= 1
        return True