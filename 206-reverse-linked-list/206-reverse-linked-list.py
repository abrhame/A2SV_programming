# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # use three two pointers
        # prev => the new Linked list
        # next => used to store the next value of the current
        # curr => we add the current to the tail of the prev lincurr = head
        
        curr = head
        prev = None
        next_ = None
        while curr:
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_
    
        return prev