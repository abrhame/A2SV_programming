var numIdenticalPairs = function(nums) {
    let ans =[]
    for(let i = 0; i<nums.length; i++){
       for(let j = i+1;j<nums.length;j++){
           if(nums[i]===nums[j]){
               ans.push([i,j])
               
           }
       }
    }
    console.log(ans)
    return ans.length;
};
