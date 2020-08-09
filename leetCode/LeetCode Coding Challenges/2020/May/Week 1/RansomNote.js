/*
Given an arbitrary ransom note string and another string containing letters from all the magazines, 
write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

You may assume that both strings contain only lowercase letters.
*/

/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
var canConstruct = function(ransomNote, magazine) {
    const neededLetters = {};
    ransomNote.split("").forEach(letter => {
        if (neededLetters[letter]) {
            neededLetters[letter] += 1;
        } else {
            neededLetters[letter] = 1;
        }
    });

    magazine.split("").forEach(letter => {
        if (neededLetters[letter] !== undefined && neededLetters[letter] > 0) {
            neededLetters[letter] -= 1;
        }
    });

    return Object.values(neededLetters).every(value => value === 0);
};