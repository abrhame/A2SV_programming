var MyQueue = function() {
   this.array = []; 
};

/** 
 * @param {number} x
 * @return {void}
 */
MyQueue.prototype.push = function(x) {
    
    return this.array.push(x);
};

/**
 * @return {number}
 */
MyQueue.prototype.pop = function() {
    

    return this.array.shift();
};

/**
 * @return {number}
 */
MyQueue.prototype.peek = function() {
    return this.array[0]
};

/**
 * @return {boolean}
 */
MyQueue.prototype.empty = function() {
    if(this.array.length === 0){
        return true;
    }else{
        return false;
    }
};
