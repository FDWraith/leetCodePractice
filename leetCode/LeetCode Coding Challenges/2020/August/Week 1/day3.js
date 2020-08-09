/*
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false


Constraints:

s consists only of printable ASCII characters.
*/

const stripNonAlphanumerics = (str) => {
    return str.split('').filter(letter => letter.match(/[A-Za-z0-9]/g)).join('');
}

const isPalidrome = (str) => {
    str = str.toLowerCase();
    str = stripNonAlphanumerics(str);
    let index = 0;
    const len = str.length;
    while (index <= len / 2 - 1) {
        if (str.charAt(index) !== str.charAt(len - index - 1)) {
            return false;
        }
        index += 1;
    }
    return true;
}

console.log(isPalidrome('a')); // expects true
console.log(isPalidrome('raCecar')); // expects true
console.log(isPalidrome('a-A')); // exptects true
console.log(isPalidrome('c a n n o t')) // expects false