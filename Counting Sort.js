function countingSort(arr) {
    // Write your code here
    let answer = new Array(arr.length).fill(0);
    let b = new Array(arr.length).fill(0);
    for(let i= 0; i<arr.length - 1; i++){
        answer[arr[i]]+=1; 
    }
    for(let i= 1; i<arr.length - 1; i++){
        answer[i] = answer[i-1]+answer[i]; 
        b[]
    }
    console.log(answer)
 return answer;
}
