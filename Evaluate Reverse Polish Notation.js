var evalRPN = function(tokens) {
        var stack = [];
    var right, left;
    for (i of tokens) {
        switch(i) {
            case '+':
                stack.push(stack.pop() + stack.pop());
                break;
            case '-':
                right = stack.pop();
                left = stack.pop();
                stack.push(left - right);
                break;
            case '*':
                stack.push(stack.pop() * stack.pop());
                break;
            case '/':
                right = stack.pop();
                left = stack.pop();
                stack.push(left / right | 0);
                break;
            default:
                stack.push(parseInt(i));
        }
    }
    return stack[0];
};
