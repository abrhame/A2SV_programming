       var kClosest = function(points, k) {
        let pair;
        let distance = [];
        let sDist = [];
        let ans=[];
        points.map(point => {
            pair = {key:point, value:Math.sqrt(point[0]*point[0] + point[1]*point[1])};
            distance.push(pair)
        })
       distance.sort((a,b)=>a.value-b.value);
       distance[distance.length-1].value>k ? sDist = (distance.slice(0,k)):sDist = distance;
        for(let i=0;i<sDist.length;i++){
            ans.push(sDist[i].key);
        }
        return ans;
    };
    
