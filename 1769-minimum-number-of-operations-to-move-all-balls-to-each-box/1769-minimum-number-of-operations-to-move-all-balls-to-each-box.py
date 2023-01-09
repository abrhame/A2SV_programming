class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # p1 = 0
        # p2 = 0
        # ans = []
        # sum_ = 0
        # while p1 < len(boxes):
        #     if boxes[p2] == "1":
        #         sum_ += abs(p2 - p1)
        #         p2 += 1
        #     if p2 == (len(boxes) - 1):
        #         ans.append(sum_)
        #         sum_ = 0
        #         p1 += 1
        #         p2 = 0
        # return ans
        
        ans = []
        
        for i in range(len(boxes)):
            step = 0
            for j in range(len(boxes)):
                if boxes[j] == "1":
                    step += abs(j - i)
            ans.append(step)
            
        return ans