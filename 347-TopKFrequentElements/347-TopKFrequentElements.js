/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    const map = new Map();

    for(num of nums){
        if(map.has(num)){
            map.set(num, (map.get(num)) + 1)
        }
        else {
            map.set(num, 1)
        }
    }

    const sorted = Array.from(map.entries()).sort((a, b) => b[1] - a[1]);
    const output = []
    
    for(let i = 0; i < k; i++){
        const [val, freq] = sorted[i]
        output.push(val)
    }
    return output
};