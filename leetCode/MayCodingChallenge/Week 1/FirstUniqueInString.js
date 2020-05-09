/*
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
*/

/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function(s) {
    const nonRepeats = {};
    const seen = new Set([]);
    s.split("").forEach((letter, index) => {
        if (!seen.has(letter)) {
            nonRepeats[letter] = index;
            seen.add(letter);
        } else {
            nonRepeats[letter] = undefined;
        }
    });

    const results = Object.values(nonRepeats).filter(v => v !== undefined)

    return results.length !== 0 ? Math.min(...results) : -1;
};