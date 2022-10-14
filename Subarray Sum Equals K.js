var subarraySum = function (nums, k) {
  let map = new Map();
  map.set(0, 1);
  let res = 0;

  let sum = 0;
  for (let i = 0; i < nums.length; i++) {
    sum += nums[i];
    let diff = sum - k;

    if (map.has(diff)) {
        console.log(map.get(diff))
      res += map.get(diff);

    }

    if (map.has(sum)) {
      map.set(sum, map.get(sum) + 1);
    } else {
      map.set(sum, 1);
    }
  }
  return res;
};
