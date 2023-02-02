# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # use two pointers that go in parallel 
        # if the two consecutive elments are the same remove the current element
        
        if head == None or head.next == None:
            return head
        prev = head
        cur = head.next
        
        while cur:
            # remove duplicate elemtnts
            if cur.val == prev.val:
                prev.next = cur.next
                cur = cur.next
            
            else:
                prev = cur
                cur = cur.next


        return head