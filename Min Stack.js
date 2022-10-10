var MinStack = function() {
        this.array = [];
        this.sorted = [];
};

/** 
 * @param {number} val
 * @return {void}
 */
MinStack.prototype.push = function(val) {
    this.array.push(val);
    if(this.sorted.length === 0){
        this.sorted.push(val);
    }else{
        this.sorted.push(Math.min(val,this.sorted[this.sorted.length-1]));
    }
    
    return this.array;
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
    this.array.pop();
    this.sorted.pop();
    return this.array;
};

/**
 * @return {number}
 */
MinStack.prototype.top = function() {
    return this.array[this.array.length -1]
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function() {
    return this.sorted[this.sorted.length - 1];
};
