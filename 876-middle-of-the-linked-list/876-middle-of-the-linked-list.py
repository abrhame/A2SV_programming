# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # use fast and slow pointers. the fast pointer moves twice the slow pointer
        # when the fast pointer finishes the linked list the slow pointer will be at the middle of the linked list
        
        fast = head
        slow = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow