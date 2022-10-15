var maxSumTwoNoOverlap = function(nums, firstLen, secondLen) {
    const createSum = breakpoint => {
        console.log(breakpoint)
        let res = [];
        let sum = 0;
        let left = 0;
        for (let i = 0; i < nums.length; i++) {
            sum += nums[i];
            if (i >= breakpoint) {
                sum -= nums[left];
                left++;
            }
            res.push(sum);
        }
        return res;
    }
    
	// Create sum results for first and second length.
    const sum1 = createSum(firstLen);
    const sum2 = createSum(secondLen);
    let max = -Infinity;

	// Check the max possible non-overlaping sum. Start from first. 
    for (let i = firstLen - 1; i < nums.length; i++) {
        for (let j = i + secondLen; j < nums.length; j++) {
            let sum = sum1[i] + sum2[j];
            max = Math.max(sum, max);
        }
    }
	// Check the max possible non-overlapping sum. Start from second. 
    for (let  i = secondLen - 1; i < nums.length; i++) {
         for (let j = i + firstLen; j < nums.length; j++) {
            let sum = sum2[i] + sum1[j];
            max = Math.max(sum, max);
        }
    }
    return max;
};
