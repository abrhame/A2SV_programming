function countingValleys(steps, path) {
    // Write your code here
    let seaLevel = 0;
    let valley = 0;
    for(let i= 0; i < steps; i++){
        if(path[i] === 'U'){
            seaLevel+=1;
        }
        else{
            seaLevel-=1;
        }
        if((path[i]==='U') && (seaLevel===0)){
            valley+=1;
            
        }
        
    }
    return valley;

}
