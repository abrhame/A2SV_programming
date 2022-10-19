function insertionSort1(n, arr) {
    // Write your code here
    let target = arr[n-1];
    while(arr[n-2] > target) {
        arr[n-1] = arr[n-2];
        console.log(...arr);
        n--;
    }
    arr[n-1] = target;
    console.log(...arr);
}
