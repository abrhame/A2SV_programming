var corpFlightBookings = function(bookings, n) {
    let answer = new Array(n).fill(0);
    console.log(answer)
        for (let i=0; i<bookings.length; i++) {
            answer[bookings[i][0]-1] += bookings[i][2];
            if (bookings[i][1] < n) {
               answer[bookings[i][1]] -=  bookings[i][2];
            }
        }
    console.log(answer)
        for (let i=1; i<n; i++) {
            answer[i]+=answer[i-1];
        }
    console.log(answer)
        return answer;

};
