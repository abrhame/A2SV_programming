var numberOfSubarrays = function(nums, k) {
        let count = 0;                                //   nums = [1,1,2,1,1]    k = 3
        let prefix = new Array(nums.length + 1);      //   prefix = [1,1,0,0,0,0]
        prefix.fill(0);
        let odd = 0;
  
        // traverse in the array
        for (let i = 0; i < nums.length; i++)
        {
            prefix[odd]++;   //
  
            // if array element is odd
            if ((nums[i] & 1) == 1)
                odd++;  //2
                                                         
            // when number of odd
            // elements >= M
            if (odd >= k)   //1>3
                count += prefix[odd - k];
        }
  
        return count;
    }
