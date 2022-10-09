var moveZeroes = function(nums) {
	let p1 = 0;
    let p2 = 0;
    for(p2;p2<nums.length;p2++){
        if(nums[p2] !== 0){
            [nums[p1],nums[p2]] = [nums[p2],nums[p1]]
            p1++;
        }
    }
	return nums;  
};
