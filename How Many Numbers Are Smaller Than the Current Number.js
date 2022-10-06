var smallerNumbersThanCurrent = function(nums) {
    let arr = [];
    nums.map(n => {
        let i = 0;
        nums.forEach(nn => {
            if(n>nn) i++;
        });
        
        arr.push(i);
    });
    return arr;
};
