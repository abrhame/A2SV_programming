var bagOfTokensScore = function(tokens, power) {
    tokens.sort((a, b) => a - b);
    
    let score = 0, max = 0, left = 0, right = tokens.length - 1;
    
    while(left <= right) {
        if(power >= tokens[left]) {
            power -= tokens[left];
            score++;
            left++; 
        } else if(score >= 1) {
            power += tokens[right];
            score--;
            right--;
        } else {
            break;
        }
        
        max = Math.max(max, score);
    }
    
    return max;
};
