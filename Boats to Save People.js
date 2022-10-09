var numRescueBoats = function(people, limit) {
    people.sort((a, b) => a - b);
    let small = 0;
    let big = people.length -1 ;
    let boat = 0;
    while(small<=big){
        if(people[small]+people[big]<=limit) small++; 
        big--;
        boat++;
    }
    return boat;
};
