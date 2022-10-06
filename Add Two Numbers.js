    var addTwoNumbers = function(l1, l2) {
    let head = new ListNode();
    let tail = head;
    
    let sum = 0;
    let carry = 0;
    
    while(l1 || l2 || sum>0){
        if(l1){
            sum+=l1.val;
            l1 = l1.next;
        }
        if(l2){
            sum+=l2.val;
            l2 = l2.next;
        }
        carry = Math.floor(sum/10);
        sum = sum%10;
        let newNode = new ListNode(sum);
        tail.next = newNode;
        tail = newNode;
        sum = carry;
        carry = 0;
    }
 return head.next;
};
