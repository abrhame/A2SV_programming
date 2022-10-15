var NumMatrix = function(matrix) {
    let n = matrix.length , m = matrix[0].length;
    this.sum = Array(n+1).fill().map(()=>Array(m+1).fill(0)); 
    for( let i = 1 ; i <= n ; i++ ){
        for( let j = 1 ; j <= m ; j++ ){
            this.sum[i][j] = this.sum[i-1][j] + this.sum[i][j-1]-this.sum[i-1][j-1] + matrix[i-1][j-1];
        }
    } 
};

/** 
 * @param {number} row1 
 * @param {number} col1 
 * @param {number} row2 
 * @param {number} col2
 * @return {number}
 */
NumMatrix.prototype.sumRegion = function(row1, col1, row2, col2) {
     return this.sum[row2+1][col2+1] - this.sum[row2+1][col1] - this.sum[row1][col2+1] + this.sum[row1][col1]; 
};
