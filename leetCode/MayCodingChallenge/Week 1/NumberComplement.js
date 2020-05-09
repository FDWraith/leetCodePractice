/*
Given a positive integer num, output its complement number. 
The complement strategy is to flip the bits of its binary representation.

 

Example 1:

Input: num = 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
Example 2:

Input: num = 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
 

Constraints:

The given integer num is guaranteed to fit within the range of a 32-bit signed integer.
num >= 1
You could assume no leading zero bit in the integer’s binary representation.
This question is the same as 1009: https://leetcode.com/problems/complement-of-base-10-integer/
*/

/**
 * @param {number} num
 * @return {number}
 */
var findComplement = function(num) {
    function asBin(num) {
        let start = 1;
        while (num > start) {
            start *= 2;
        }

        let bits = [];
        while (start > 1) {
            if (num >= start) {
                bits.push(1);
            } else {
                bits.push(0);
            }

            num = num % start;
            start /= 2;
        }

        // concat the last bit
        bits.push(num);

        if (bits[0] === 0) {
            bits = bits.slice(1);
        }

        return bits.join("");
    }

    function flipBits(bin) {
        return bin.split("").map(bit => bit === "1" ? "0" : "1").join("");
    }

    return parseInt(flipBits(asBin(num)), 2);

};