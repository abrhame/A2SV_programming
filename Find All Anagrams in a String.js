var findAnagrams = function(s, p) {
    let L=0,R=0,windowSize = p.length, count=0, map = new Map(), result=[];
    for(let ch of p) {
        if(!map.has(ch)) {
            map.set(ch,1);
        } else {
            let c = map.get(ch);
            map.set(ch,c+1);
        }
    }
    count = map.size;
    while(R<s.length) {
        if(map.has(s[R])) {
            let c = map.get(s[R]);
            c--;
            if(!c) {
                count--;
            }
            map.set(s[R],c);
        }
        if(R-L+1 < p.length) {
            R++;
        } else if(R-L+1 === p.length) {
            if(count === 0){
                result.push(L);
            }
            if(map.has(s[L])) {
                let c = map.get(s[L]);
                c++;
                if(c===1) {
                    count++;
                }
                map.set(s[L],c);
            }
            L++;
            R++;
        }
    }
    return result;
};
