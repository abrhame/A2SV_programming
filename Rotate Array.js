var rotate = function(nums, k) {
   k=k%nums.length;
    console.log(k)
    let i = 0;
    let j = nums.length - 1;
    swap(nums,i,j);
    swap(nums,i,k-1);
    swap(nums,k,j);
    return nums;
};

function swap(nums,i,j){
    
    while(i<j && nums.length>1){
        [nums[i],nums[j]] = [nums[j],nums[i]];
        i++;
        j--;
    }
}
