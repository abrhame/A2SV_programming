var mergeTwoLists = function(list1, list2) {
    let dummyHead = new ListNode(0);
    let p = dummyHead;
    while(list1!==null && list2!==null){
        if(list1.val < list2.val){
            p.next = list1;
            list1 = list1.next;
        }else{
            p.next = list2;
            list2 = list2.next;
        }
        p = p.next;
    }
    if(list1 !== null) p.next = list1;
    if(list2 !== null) p.next = list2;
    return dummyHead.next;
};
