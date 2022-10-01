var minSetSize = function(arr) {
    let map = {};
    arr.forEach(num => {
        if(map[num] === undefined){
            map[num]=0;
        }
        map[num]++;
    });
    const n = arr.length;
    let cur = n, res = 0;
    
    const list = Object.keys(map).sort((a,b)=>map[b] - map [a]);
    for(let i =0; i<list.length; i++) {
        const num = list[i];
        cur -= map[num];
        res++;
        if(cur <= n/2) {
            return res;
        }
    }
    return res;
};
