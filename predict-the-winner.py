class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def winner(arr,l,r,turn):
            if l == r:
                return [arr[l],0] if turn else [0, arr[l]]
            if turn:
                left=winner(arr,l+1,r,not turn)
                left[0] += arr[l]
                right=winner(arr,l,r-1,not turn)
                right[0] += arr[r]
                if left[0] > right[0]:
                    return left
                return right
            else:
                left=winner(arr,l+1,r,not turn)
                left[1] += arr[l]
                right = winner(arr,l,r-1,not turn)
                right[1] += arr[r]
                if left[1] > right[1]:
                    return left
                return right


        player = winner(nums,0,len(nums)-1,True)
        return player[0] >= player[1]