  selectionSort(arr,n){
   //code here
    for(let i =0; i<n;i++){
        for(let j = i+1; j< n; j++){
            if(arr[i]>arr[j]){
                let k = arr[i];
                arr[i] = arr[j];
                arr[j] = k;
            }
            

        }

    }

    return arr;
  }
