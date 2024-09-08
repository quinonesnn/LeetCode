/**
 * @param {number[][]} accounts
 * @return {number}
 */
var maximumWealth = function(accounts) {
    let wealth = 0;

    function addArr(total, num) {
        return total + num;
    }
    
    if (accounts.length === 1){
        return accounts[0].reduce(addArr)
    }

    for(let i = 0; i < accounts.length - 1; i++){
        let curr = Math.max(accounts[i].reduce(addArr), accounts[i+1].reduce(addArr))
        console.log(curr)
        if(curr > wealth){
            wealth = curr
        }
    }
    return wealth
};