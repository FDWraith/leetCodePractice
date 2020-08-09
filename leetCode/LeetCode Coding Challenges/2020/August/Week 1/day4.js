/*
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true
Example 2:

Input: 5
Output: false
Follow up: Could you solve it without loops/recursion?
*/

const isPowerOfFour = (num) => {
    if (num === 0) {
        return false;
    }

    let count = 0;
    while (num % 2 === 0) {
        count += 1;
        num = num / 2;
    }
    return num === 1 && count % 2 === 0;
}

const isPowerOfFourNoLoops = (num) => {
    // first portion checks that num is divisible by 2
    // second portion checks that the num before is divisible by 3
    return (num & (num - 1) === 0) && (num - 1) % 3 === 0
}

console.log(isPowerOfFour(4)); // expects true
console.log(isPowerOfFour(16)); // expects true
console.log(isPowerOfFour(20)); // expects false
console.log(isPowerOfFour(5));  // expects false
console.log(isPowerOfFour(32)); //expects false