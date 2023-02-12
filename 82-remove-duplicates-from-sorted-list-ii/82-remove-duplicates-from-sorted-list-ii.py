# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        while head and head.next:
            if head.val == head.next.val:
                val = head.val
                head = head.next.next
                while head and head.val == val:
                    head = head.next
            else:
                curr.next = head
                curr = curr.next
                head = head.next
        curr.next = head
        return dummy.next
                
                
        