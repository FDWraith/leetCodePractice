/*
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. 
Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
*/

/*
Test cases
[0, 0, 0] n => 0
[1, 2, 3, 4] 4 => 6
[1, -1, 0, 2] 3 => 3
[0, 3, 5, 9] 10 => 8

Theory:
Obvious solution: generate all combinations of numbers, and find the closest sum. Runtime would be O(n^3), maybe reduced with some optimizations
Optimization to obvious solution:                   
                   => Sort the array. For every num in the array, we can "include" it as one of the possible numbers
                   => Create left + right pointers at the ends of the array. Move pointers closer to the "included" number, depending on dist from target
                   => This would create a runtime of O(n^2 + nlogn)

Slightly more clever: Since we only care about the sum, we don't really need the combination of numbers; just playing with values should be enough
                   => Use a similar pointer system and sorted arr, but this time start the "center" pointer right by the left one.
                   => Store the "closest" value so far
                   => Bounce the "center" pointer between the left and right pointer?
                   
*/

function sum3Closest(nums, target) {
    if (nums.length < 3) return nums.reduce((a, b) => a + b, 0);

    nums.sort((a,b) => a-b);
        
    let closest = nums[0] + nums[1] + nums[2];
    let tryIndex = 0;
    while (tryIndex < nums.length - 2) {
        let leftIndex = tryIndex + 1;
        let rightIndex = nums.length - 1;
        while (leftIndex < rightIndex) {
            let sum = nums[tryIndex] + nums[leftIndex] + nums[rightIndex];
            if (sum === target) return target;

            let closeness = sum - target;
            
            if (Math.abs(closeness) < Math.abs(target - closest)) {
                closest = sum;
            }
            
            if (closeness > 0) {
                rightIndex -= 1;
            } else if (closeness < 0) {
                leftIndex += 1;
            }
        }
        tryIndex += 1;
    }

    return closest;
}


console.log(`Actual: ${sum3Closest([0,0,0], 3)}, Expected: 0`);
console.log(`Actual: ${sum3Closest([1,2,3], 3)}, Expected: 6`);
console.log(`Actual: ${sum3Closest([1,0,0,1], 3)}, Expected: 2`);
console.log(`Actual: ${sum3Closest([4,1,3,-8,8], 0)}, Expected: 1`);
console.log(`Actual: ${sum3Closest([0,3,5,9], 10)}, Expected: 8`);
console.log(`Actual: ${sum3Closest([1,2,4,8,16,32,64,128], 82)}, Expected: 82`);
