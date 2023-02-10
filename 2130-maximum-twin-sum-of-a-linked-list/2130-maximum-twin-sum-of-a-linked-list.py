# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow=head
        fast=head
        
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            
        # start from the middle of the element and reverse the linked list
        prev=None
        
        while slow:
            tmp=slow.next
            slow.next=prev
            prev=slow
            slow=tmp
        res = 0   
        while prev:
            twin_sum=prev.val+head.val
            if twin_sum > res:
                res = twin_sum
            prev = prev.next
            head = head.next
            
        return res
      
            
            
    
        