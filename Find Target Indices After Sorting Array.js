var targetIndices = function(nums, target) {
    let idx = [];
    for(let i = 0; i<nums.length; i++){
        for(let j = 0; j< nums.length;j++){
            if(nums[j]>nums[j+1]){
              [nums[j],nums[j+1]] = [nums[j+1],nums[j]];
            }

        }

        }
        console.log(nums)
        let i;
            for(i = 0; i< nums.length; i++){
                if(nums[i]===target){
                 (idx.push(i));
                }  
            }
            console.log(idx);
            return idx;
        }
