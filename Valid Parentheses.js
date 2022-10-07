var isValid = function(s) {
    let stack = [];
    for(let i = 0; i<s.length; i++){
        
          if((stack[stack.length-1] ==='(' && s[i]===')')||(stack[stack.length-1] ==='{' && s[i]==='}') || (stack[stack.length-1] ==='[' && s[i]===']')){
              stack.pop();
          }else{
              stack.push(s[i])
              console.log(stack)
          }
    }
  return stack.length === 0;
};
