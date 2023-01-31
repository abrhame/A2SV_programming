# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # we can create two linked lists 
        # the first one is to store valuse that are less than the x
        # the second list is to store the linked lsit that are greater than or equal to x
        
        small  = ListNode(0)
        large = ListNode(0)
        s = small
        l = large
        while head:
            if head.val < x:
                s.next = head
                s = head
            else:
                l.next = head
                l = head
            head = head.next
        l.next = None
        s.next = large.next
        head = small.next
        return head