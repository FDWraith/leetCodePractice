/*
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2

*/

/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    const counts = {};
    const limit = Math.floor(nums.length / 2);
    let result = -1;
    nums.forEach(num => {
        counts[num] = counts[num] === undefined ? 1 : counts[num] + 1;
    });
    
    Object.entries(counts).forEach(([num, count]) => {
        if (count > limit) {
            result = num;
        }
    })
    
    return result;
};