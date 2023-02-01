# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # # find the end of the linked list and prev of the end.
        # # make the end of the linked list the head and the prevnext to None
        # # do this operation k times
        # if not head:
        #     return
        # size = 0
        # for i in range(k):
        #     curr = head
        #     prev = None
        #     while curr.next != None:
        #         prev = curr
        #         curr = curr.next
        #         size += 1
        #     if size <1:
        #         return head
        #     prev.next = None
        #     curr.next = head
        #     head = curr
        # return head
        
        # find the end of the linked list and make the next of the end of the linked list to be head
        # find the length and update k = length-(k%length) to find the head of the new linked list
        # find the tail of the your new linked list by usung the value of k
        # make the next of tail head and disconnect the head  with tail
        
        if not head:
            return head
        # find the tail
        curr = head
        length = 1
        while curr.next:
            curr = curr.next
            length += 1
        #make it circular
        curr.next = head
        
        # find the postion of the tail after k time rotaion
        k = length - (k%length)
        
        # find the tail
        while k > 0:
            curr = curr.next
            k -= 1
        
        # make the head next of the tail and disconnect the tail
        head = curr.next
        curr.next = None
        
        return head
                