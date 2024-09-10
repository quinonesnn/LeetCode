var longestConsecutive = function(nums) {
    // Step 1: Handle the base case when the array is empty.
    if (nums.length === 0) {
        return 0;
    }

    let numSet = new Set(nums);

    let cnt = 1;        // Initialize a counter for the current consecutive sequence length.
    let longest = 1;    // Initialize a variable to store the maximum consecutive sequence length.

    // Step 3: Iterate through the elements of 'nums'.
    for (let num of nums) {
        // Step 4: If the current element 'num' is the start of a sequence (no 'num-1' in 'numSet'),
        if (!numSet.has(num - 1)) {
            let x = num;  // Update 'x' to the current element 'num'.

            // Step 5: While consecutive elements exist in 'numSet', increment 'cnt' and 'x'.
            while (numSet.has(x + 1)) {
                cnt++;
                x++;
            }
        }
        
        // Step 6: Update 'longest' with the maximum of 'longest' and 'cnt'.
        longest = Math.max(longest, cnt);
    }

    // Step 7: Return 'longest' as the result.
    return longest;
};

