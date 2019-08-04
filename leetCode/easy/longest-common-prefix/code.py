"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""

"""
Testing:

["hello", "hel", "h"] => "h"
["hello", "hel", "h", ""] => ""

["world", "helloworld", "wew"] => ""
[] => ""
["one"] => "one"

O(n^2) would be compare everything to each other
O(n) would be generating longest common prefix as I go through the array
ex. 
LCP("hello", "hel") => "hel"
LCP("hel", "h") => "h"

And so on.
"""

# Compares two values to get the longest common prefix
def lcp_single(v1, v2):
    common = ""
    chars_to_compare = min(len(v1), len(v2))
    
    for i in range(chars_to_compare):
        if (v1[i] == v2[i]):
            common += v1[i];
        else:
            return common
    return common

     
# Compares multiple values to get longest common prefix of all
def lcp(value_array):
    if (len(value_array) == 0):
        return ""
    
    if (len(value_array) == 1):
        return value_array[0]
    
    lcp_so_far = lcp_single(value_array[0], value_array[1])
    for value in value_array[2:]:
        lcp_so_far = lcp_single(lcp_so_far, value)
        if (lcp_so_far == ""):
            return ""

    return lcp_so_far

# Testing 
print "Actual: '" + lcp(["hello", "hel", "h"]) + "', Expected: 'h'"
print "Actual: '" + lcp(["hel", "hello", "h"]) + "', Expected: 'h'"
print "Actual: '" + lcp(["hello", "hel", "h", ""]) + "', Expected: ''"
print "Actual: '" + lcp(["hello"]) + "', Expected: 'hello'"
print "Actual: '" + lcp([]) + "', Expected: ''"
print "Actual: '" + lcp(["car", "cat", "dog"]) + "', Expected: ''"
