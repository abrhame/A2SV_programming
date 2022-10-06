var maxCoins = function(piles) {
    piles.sort((a,b)=>a-b)
    let j=piles.length-2,
	ans=0;
    
    // you have to iterate only piles.length/3. unless it will result in 
    // incorrect answer because j takes unnssray value
    for(let i=0;i<piles.length/3;i++){
        ans+=piles[j];
        j=j-2;
    }
    return ans;
    
};
