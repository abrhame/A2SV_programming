# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # we can use a stack datastructure.
        # first we iterate over the two linked lists and we find thir sum and we store it to the stack.
        # at last starting from the top of the stack and if the elments is greater than 9 we add it to the next element.
        # AT LAST WE CAN FORM A NEW LINKEDLIST USING THE STACK
        
        dummy = ListNode(0)
        stack = []
        ans = []
        while l1 and l2:
            stack.append(l1.val + l2.val)
            l1 = l1.next
            l2 = l2.next
        while l1:
            stack.append(l1.val)
            l1 = l1.next
        
        while l2:
            stack.append(l2.val)
            l2 = l2.next
            
        r = 0   
        for num in stack:
            num = num + int(r)
            r = 0
            if num > 9:
                num = str(num)
                r,s = num[0],num[1]
                ans.append(int(s))
            else:
                if num < 10:
                    ans.append(num)
                else:
                    num = str(num)
                    r,s = num[0],num[1]
                    ans.append(int(s))
                    
        r = int(r)
        if r > 0:
            ans.append(r)
        
        cur = dummy
        for num in ans:
            Node = ListNode(num)
            cur.next = Node
            cur = Node
        return dummy.next          
            
                
                
                