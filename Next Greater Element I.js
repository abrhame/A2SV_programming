var nextGreaterElement = function(nums1, nums2) {
    let result = [];
    for(let i = 0; i<nums1.length; i++){
        let x = -1;
        for(let j = nums2.length-1; nums2[j] != nums1[i] ; j--){
            if(nums1[i] < nums2[j]){
                x = nums2[j];
        }
    }
        result.push(x)
    }
    return result;
};
