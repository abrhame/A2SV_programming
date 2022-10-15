var totalFruit = function(fruits) {
    const basket = new Map();
    let left = 0, maxLen = 0;
	for (let right = 0; right < fruits.length; right++) {
		const rightFruit = fruits[right];
        basket.set(rightFruit, basket.get(rightFruit) + 1 || 0);
        while (basket.size > 2) {
            const leftFruit = fruits[left];
            if (basket.get(leftFruit) === 0) {
                basket.delete(leftFruit);
            } else {
                basket.set(leftFruit, basket.get(leftFruit) - 1);
            }
            left++;
        }
        maxLen = Math.max(maxLen, right - left + 1);
    }
    return maxLen;
};
