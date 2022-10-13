	var partitionLabels = function (s) {
		let hash = {};

		for (let i = 0; i < s.length; i++) {
			hash[s[i]] = i;
		}
		let result = [];
		let start = 0;
		let last = 0;

		for (let i = 0; i < s.length; i++) {
			last = Math.max(last, hash[s[i]]);
			if (i == last) {
				result.push(last - start + 1);
				start = last + 1;
			}
		}

		return result;
	};
