/**
 * @param {number} num
 * @return {number}
 */
var numberOfSteps = function(num) {
    let steps = 0;
    let curr = num;
    while(curr != 0){
        if(curr % 2 == 0){
            curr = (curr / 2);
            steps++;
        } 
        else {
            curr--;
            steps++;
        }
    }
    return steps;
};