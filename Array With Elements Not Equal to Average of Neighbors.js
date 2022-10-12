var rearrangeArray = function(nums) {
    let answer = [];
    let left = 0;
    let right = nums.length-1;
    nums.sort((a,b)=> a-b);
    while(left < right){
        answer.push(nums[left++]);
        answer.push(nums[right--]);
    }
    if(left === right){
        answer.push(nums[left]);
    }
    return answer;
};
