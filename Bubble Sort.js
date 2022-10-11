function countSwaps(a) {
    // Write your code here
    let count = 0;
    for(let i =0; i<a.length;i++){
        for(let j = 0; j<a.length; j++){
            if(a[j]>a[j+1]){
                [a[j],a[j+1]] = [a[j+1],a[j]];
                count++;
            }
        }
    }
    console.log(`Array is sorted in ${count} swaps.`)

    console.log(`First Element: ${a[0]}`)

    console.log(`Last Element: ${a[a.length -1]}`)
}
