# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # travesrs through the linked list and put all the odd elements on diffrernt places and all the even indiceis  on separate places
        
        even = ListNode()
        odd = ListNode()
        e = even
        o = odd
        cur = head
        pos = 0
        while cur:
            if pos % 2 == 0:
                e.next = cur
                e = e.next
            else:
                o.next = cur
                o = o.next
            cur = cur.next
            pos += 1
        o.next = None
        e.next = odd.next

        return even.next