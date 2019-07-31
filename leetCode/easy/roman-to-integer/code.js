/* Problem Statement
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

Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.


*/

// Test Cases: 
/*
I => 1
IV => 4
MMMCMXCIX => 3999
MMMCM => 3900
XC => 96 

Descending numerals mean addition
Ascending means subtraction (from what comes next)

There will be at most 1 ascending numeral before the descending pattern resumes
eg. IX, or XC, or CD, etc...

so at most, we have to look ahead one letter.
*/

// Convert a single numeral to its simple value
function convertSingleNumeral(n) {
    switch(n) {
        case "I":
            return 1;
        case "V":
            return 5;
        case "X":
            return 10;
        case "L":
            return 50;
        case "C":
            return 100;
        case "D":
            return 500;
        case "M":
            return 1000;
        default:
            return 0;
    }
}

function convertRomanToInteger(r) {
    const numerals = r.split("");
    
    let totalValue = 0;
    
    for (let currIdx = 0; currIdx < numerals.length; currIdx += 1) {
        let currValue = convertSingleNumeral(numerals[currIdx]); 
        if (currIdx + 1 < numerals.length) {
            let nextValue = convertSingleNumeral(numerals[currIdx + 1]);
            if (nextValue > currValue) {
                totalValue += nextValue - currValue;
                currIdx += 1;
            } else {
                totalValue += currValue;
            }
        } else {
            totalValue += currValue;
        }        
    }

    return totalValue;
}


// Refactor to Optimize and Reduce Redundancies
function convertRomanToIntegerOptimized(r) {
    const numerals = r.split("");
    
    let prevValue = convertSingleNumeral(numerals[0]);
    let totalValue = prevValue;

    for (let currIdx = 1; currIdx < numerals.length; currIdx += 1) {
        let currValue = convertSingleNumeral(numerals[currIdx]); 
        if (currValue > prevValue) {
            totalValue -= 2 * prevValue;
        }
        totalValue += currValue;
        prevValue = currValue;
    }

    return totalValue;
}

// Without Using Split
function convertRomanToIntegerWithoutSplit(r) {
    let prevValue = convertSingleNumeral(r.charAt(0));
    let totalValue = prevValue;

    for (let currIdx = 1; currIdx < r.length; currIdx += 1) {
        let currValue = convertSingleNumeral(r.charAt(currIdx)); 
        if (currValue > prevValue) {
            totalValue -= 2 * prevValue;
        }
        totalValue += currValue;
        prevValue = currValue;
    }

    return totalValue;
}


// Executing Tests
console.log(`Value: ${convertRomanToInteger("I")}, Expected: 1`);
console.log(`Value: ${convertRomanToInteger("VI")}, Expected: 6`);
console.log(`Value: ${convertRomanToInteger("IX")}, Expected: 9`);
console.log(`Value: ${convertRomanToInteger("III")}, Expected: 3`);
console.log(`Value: ${convertRomanToInteger("MMMCMXCIX")}, Expected: 3999`);
console.log(`Value: ${convertRomanToInteger("CDL")}, Expected: 450`);
console.log(`Value: ${convertRomanToInteger("CCCIX")}, Expected: 309`);

// Time Difference
console.time();
convertRomanToInteger("MMMCMXCIX"); 
console.timeEnd(); // 0.055 ms

console.time();
convertRomanToIntegerOptimized("MMMCMXCIX");
console.timeEnd(); // 0.052 ms

console.time();
convertRomanToIntegerWithoutSplit("MMMCMXCIX");
console.timeEnd(); // 0.045 ms



