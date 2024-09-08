/**
 * @param {number} n
 * @return {string[]}
 */
var fizzBuzz = function(n) {
    let out = []
    for(let i = 1; i < n + 1; i++){
        if(i % 3 == 0 && i % 5 == 0){
            out.push("FizzBuzz")
            continue
        }
        if(i % 3 == 0){
            out.push("Fizz")
            continue
        }
        if(i % 5 == 0){
            out.push("Buzz")
            continue
        }
        else{
            out.push(String(i))
        }
    }
    return(out)
};