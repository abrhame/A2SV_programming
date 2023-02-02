# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # find the length of the linked list
        # find the node to be removed starting from the head of the linked list
        # remove the node
        
        cur = head
        length = 0
        while cur:
            cur = cur.next
            length += 1
        if length == 1:
            return None
        k = length - n
        cur = head
        if k == 0:
            return head.next
        for _ in range(k-1):
            cur = cur.next
        cur.next = cur.next.next
        return head