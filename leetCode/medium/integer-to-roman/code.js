/*
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.
*/

// Test Cases
/*
1 -> I
5 -> V
4 -> IV
9 -> IX
6 -> VI
399 -> CCCXCIX
400 -> CD
*/


// Thought Process
/*
break down numbers into ranges / easily compostable pieces ??

how many "numerals" can I fit (starting with largest numerals0

ex. 3999 -> 3 M,
999 left, 
can I still fit another M ? 
No. 
How many D can I fit? 
1 D
499 --> Problem here is that we don't want to do this... 
We want next numerals to be CM 
and then 

I don't have to be confined to exact numerals (for breaking down stuff)
1000
900
500
400
100
90
10
9
5
4
1

Recursive solution (repeat the problem, but with an accumulator)

*/

function convertIntegerToRomanRecursive(i) {    
    function convertIntegerToRoman(i, romanStringSoFar) {
        if (i >= 1000) {
            return convertIntegerToRoman(i - 1000, romanStringSoFar + "M");
        } else if (i >= 900) {
            return convertIntegerToRoman(i - 900, romanStringSoFar + "CM");
        } else if (i >= 500) {
            return convertIntegerToRoman(i - 500, romanStringSoFar + "D");
        } else if (i >= 400) {
            return convertIntegerToRoman(i - 400, romanStringSoFar + "CD");
        } else if (i >= 100) {
            return convertIntegerToRoman(i - 100, romanStringSoFar + "C");
        } else if (i >= 90) {
            return convertIntegerToRoman(i - 90, romanStringSoFar + "XC");
        } else if (i >= 50) {
            return convertIntegerToRoman(i - 50, romanStringSoFar + "L");
        } else if (i >= 40) {
            return convertIntegerToRoman(i - 40, romanStringSoFar + "XL");
        } else if (i >= 10) {
            return convertIntegerToRoman(i - 10, romanStringSoFar + "X");
        } else if (i >= 9) {
            return convertIntegerToRoman(i - 9, romanStringSoFar + "IX");
        } else if (i >= 5) {
            return convertIntegerToRoman(i - 5, romanStringSoFar + "V");
        } else if (i >= 4) {
            return convertIntegerToRoman(i - 4, romanStringSoFar + "IV");
        } else if (i >= 1) {
            return convertIntegerToRoman(i - 1, romanStringSoFar + "I");
        } else {
            return romanStringSoFar;
        }
    }

    return convertIntegerToRoman(i, "");
}

function convertIntegerToRomanWithLoop(i) {
    let romanString = "";
    while (i > 0) {
        if (i >= 1000) {
            romanString += "M";
            i -= 1000;
        } else if (i >= 900) {
            romanString += "CM";
            i -= 900;
        } else if (i >= 500) {
            romanString += "D";
            i -= 500;
        } else if (i >= 400) {
            romanString += "CD";
            i -= 400;
        } else if (i >= 100) {
            romanString += "C";
            i -= 100;
        } else if (i >= 90) {
            romanString += "XC";
            i -= 90;
        } else if (i >= 50) {
            romanString += "L";
            i -= 50;
        } else if (i >= 40) {
            romanString += "XL";
            i -= 40;
        } else if (i >= 10) {
            romanString += "X";
            i -= 10;
        } else if (i >= 9) {
            romanString += "IX";
            i -= 9;
        } else if (i >= 5) {
            romanString += "V";
            i -= 5;
        } else if (i >= 4) {
            romanString += "IV";
            i -= 4;
        } else if (i >= 1) {
            romanString += "I";
            i -= 1;
        } else {
            // Should not reach this case
        }
    }

    return romanString;
}


// Testing
console.time("recursive");
console.log(`Actual: ${convertIntegerToRomanRecursive(1)}, Expected: I`);
console.log(`Actual: ${convertIntegerToRomanRecursive(4)}, Expected: IV`);
console.log(`Actual: ${convertIntegerToRomanRecursive(5)}, Expected: V`);
console.log(`Actual: ${convertIntegerToRomanRecursive(6)}, Expected: VI`);
console.log(`Actual: ${convertIntegerToRomanRecursive(20)}, Expected: XX`);
console.log(`Actual: ${convertIntegerToRomanRecursive(399)}, Expected: CCCXCIX`);
console.log(`Actual: ${convertIntegerToRomanRecursive(400)}, Expected: CD`);
console.log(`Actual: ${convertIntegerToRomanRecursive(3500)}, Expected: MMMD`);
console.timeEnd("recursive");

console.log("================================================");

// Testing for Loop
console.time("looping");
console.log(`Actual: ${convertIntegerToRomanWithLoop(1)}, Expected: I`);
console.log(`Actual: ${convertIntegerToRomanWithLoop(4)}, Expected: IV`);
console.log(`Actual: ${convertIntegerToRomanWithLoop(5)}, Expected: V`);
console.log(`Actual: ${convertIntegerToRomanWithLoop(6)}, Expected: VI`);
console.log(`Actual: ${convertIntegerToRomanWithLoop(20)}, Expected: XX`);
console.log(`Actual: ${convertIntegerToRomanWithLoop(399)}, Expected: CCCXCIX`);
console.log(`Actual: ${convertIntegerToRomanWithLoop(400)}, Expected: CD`);
console.log(`Actual: ${convertIntegerToRomanWithLoop(3500)}, Expected: MMMD`);
console.timeEnd("looping");
