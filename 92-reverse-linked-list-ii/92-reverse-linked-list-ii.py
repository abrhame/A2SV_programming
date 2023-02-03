# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # find the prev of the left and also store the value of the left
        # reverse all the nodes starting from the left
        # point the next of the prev to point to reversed linked list
        # store the next of the head of the reversed llinked list before reversing it
        # point the end of the reversed linked list to point to the the stored value
#         if head.next == None or left == right:
#             return head
#         dummy = ListNode(0,head)
#         cur = head
#         leftPrev = dummy
#         while cur and cur.next:
#             if cur.next.val == left:
#                 leftPrev = cur
#                 cur = cur.next
#                 break
#             cur = cur.next

#         left_N = cur
#         prev = None
#         right_next = None
#         while cur.val != right:
#             tmp = cur.next
#             cur.next = prev
#             prev = cur
#             cur = tmp
#         right_next = cur.next
#         cur.next = prev
#         prev = cur
#         leftPrev.next = prev
#         left_N.next = right_next
        
#         return dummy.next

        #reach the node at postion "left"
        dummy = ListNode(0,head)
        leftPrev, cur = dummy, head
        for i in range(left-1):
            leftPrev, cur = cur, cur.next

        # reverse from the left to right
        prev = None
        for i in range(right - left + 1):
            tmpNext = cur.next
            cur.next = prev
            prev, cur = cur, tmpNext

        # update pointers
        leftPrev.next.next = cur
        leftPrev.next = prev
        return dummy.next


        
        
        
        
        