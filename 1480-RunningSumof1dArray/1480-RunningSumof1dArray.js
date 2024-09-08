/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function(nums) {
    let arr = [nums[0]]
    let prev = nums[0]
    for (let i = 1; i < nums.length; i++){
        let sum = prev + nums[i];
        arr.push(sum)
        prev = sum
    }
    return arr
};