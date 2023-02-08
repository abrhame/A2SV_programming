# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        # # iterate over each node and find the greaeter element next to it
        # cur = head
        # ans = []
        # while cur:
        #     fast = cur.next
        #     greater = 0
        #     while fast:
        #         if fast.val > cur.val:
        #             greater = fast.val
        #             break
        #         fast = fast.next
        #     ans.append(greater)
        #     cur = cur.next
        # return ans
        
        
        pos = -1
        ans,stack = [], []
        
        while head:
            pos += 1
            ans.append(0)
            
            while stack and stack[-1][1] < head.val:
                index,val = stack.pop()
                ans[index] = head.val
                
            stack.append((pos,head.val))
            head = head.next
            
        return ans