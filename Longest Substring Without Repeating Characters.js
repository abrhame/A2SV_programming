var lengthOfLongestSubstring = function (s) {
  const map = {};
  let ans = 0;
  let start = 0;

  for (let end = 0; end < s.length; end++) {
    const char = s[end];
    map[char] = (map[char] || 0) + 1;

    while (map[char] > 1) {
      const charBefore = s[start];
      map[charBefore]--;
      if (map[charBefore] === 0) delete map[charBefore];
      start++;
    }

    ans = Math.max(ans, end - start + 1);
  }

  return ans;
};
