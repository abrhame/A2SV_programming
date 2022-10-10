var pivotIndex = function(nums) {
    this.sum = [];
    this.sum[0]=0;
    let leftsum = 0;
    for(let i = 1; i<=nums.length; i++ ){
        this.sum[i] = this.sum[i-1] + nums[i-1];
    };
    for (let i = 0; i < nums.length; ++i) {
            if (this.sum[i] === this.sum[this.sum.length - 1] - this.sum[i] - nums[i]){
               return i; 
            } 

        }
        return -1;
};
