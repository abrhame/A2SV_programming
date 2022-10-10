var reverseParentheses = function(s) {
    let stack = [];
    for(let i = 0; i<s.length; i++){

        if(s[i]!==')'){
            stack.push(s[i]);
            }else{
                let temp = [];
            while(stack[stack.length -1]!=='('){
                temp.push(stack.pop());
            }
                stack.pop();
                stack.push(...temp)
            }
        }
    
    return stack.join('');
};
