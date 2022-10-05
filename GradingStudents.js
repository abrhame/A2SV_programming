function gradingStudents(grades) {
    // Write your code here
    for(let i = 0; i<=grades.length; i++ ){
        for(let j = 0; j<=100;j++){
            if((grades[i] >= 38) && (j%5 === 0 )){
                let d = j - grades[i];
                if(d > 0 && d < 3 ){
                    grades[i] = j;
                    console.log(grades);
                }
            }
        }
        
    }
    return grades;
}
