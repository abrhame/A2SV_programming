var middleNode = function(head) {
   let p1 = head;
    let p2 = head;
    while(p2 !==null && p2.next !== null){
        p1 = p1.next;
        p2 = p2.next.next;
    }
    return p1;
};


/// another fastest(optimized) solution

var middleNode1 = function(head) {
	let currentNode = head; 
    let index = 0; //becomes the length of the linked list
    while(currentNode){
        index++;
        currentNode = currentNode.next; 
    } //O(n)
    
    let halfIndex; 
    if( index % 2 !== 0 ) {
        halfIndex = (index-1) / 2; 
    } else {
        halfIndex = index / 2; 
    } //O(1); 
    
    currentNode = head; 
    let newIndex = 0; 
    while(newIndex < halfIndex){
        currentNode = currentNode.next; 
        newIndex++
    } //O(n); 
    return currentNode; 
};

