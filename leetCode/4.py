'''

Problem Statement:

Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. 
Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, 
or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.
===============================================================================

See tests for examples that I came up with.

Python has string.strip(), which will strip any extraneous white space in the front.
We need a function numerical(c) which will check if a character c is numerical
For that matter, checking +/- can be done with sign(c), as well.

function ctoi converts single character to a number.

checking for overflow / underflow is a bit harder, because python doesn't have a min/max (in python 3.0 at least)

we might need an overflow/underflow function, such as overflow(i,n), which would check to see if 10 * i +/- n is overflow/underflow. 

'''

def atoi(s):
    """
    s - string input
    ret: 32-bit integer
    """
        
    s = s.strip()
    # check for empty strings
    if s == "":
        return 0
    
    # check to see if first non-whitespace character is either a number or a sign
    if not (numerical(s[0]) or sign(s[0])):
        return 0

    sign_ = "+"
    # determine the sign of the number
    if sign(s[0]):
        sign_ = s[0]
        s = s[1:] if len(s) > 1 else ""
        
    res = 0
    for c in s:
        # as long as it is a number
        if numerical(c) and not overflow(res, ctoi(c), sign_):
            res = res * 10 + ctoi(c)
        else:
            if numerical(c) and overflow(res, ctoi(c), sign_):
                return -2147483648 if sign_ == "-" else  2147483647
            else:
                return -1 * res if sign_ == "-" else res
    return -1 * res if sign_ == "-" else res 


def numerical(c):
    """
    c - character
    ret: boolean
    """
    return c in set(["0","1","2","3","4","5","6","7","8","9"])

def sign(c):
    """
    c - character
    ret: boolean
    """
    return c == "+" or c == "-"

def ctoi(c):
    """
    c - character
    ret: single digit number
    """
    
    num = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
    return num[c] if c in num else 0

def overflow(integer, next_digit, sign):
    """
    integer - integer
    next_digit - single digit number
    sign - "+" or "-"
    ret: boolean
    """
    
    if sign == "+":
        return (integer == 214748364 and next_digit > 7) or (integer > 214748364)
    elif sign == "-":
        return (integer == 214748364 and next_digit > 8) or (integer > 214748364)
    else:
        return False

# Tests
import unittest

class testAToI(unittest.TestCase):
    def test_numerical(self):
        self.assertEqual(numerical(""), False)
        self.assertEqual(numerical("a"), False)
        self.assertEqual(numerical("9"), True)
        self.assertEqual(numerical(" "), False)

    def test_sign(self):
        self.assertEqual(sign("+"), True)
        self.assertEqual(sign("-"), True)
        self.assertEqual(sign("h"), False)

    def test_ctoi(self):
        self.assertEqual(ctoi("1"), 1)
        self.assertEqual(ctoi("0"), 0)
        self.assertEqual(ctoi("21"), 0)

    def test_overflow(self):
        self.assertEqual(overflow(333333333, 4, "+"), True)
        self.assertEqual(overflow(333333333, 0, "-"), True)
        self.assertEqual(overflow(214748364, 8, "+"), True)
        self.assertEqual(overflow(214748364, 8, "-"), False)
        self.assertEqual(overflow(20, 1, "+"), False)
        self.assertEqual(overflow(10100236, 0, "-"), False)
        
    def test_atoi(self):
        self.assertEqual(atoi(""), 0)
        self.assertEqual(atoi("42"), 42)
        #self.assertEqual(atoi("   42"), 42)
        self.assertEqual(atoi("+ 42"), 0)
        self.assertEqual(atoi("+42"), 42)
        self.assertEqual(atoi("-42"), -42)
        self.assertEqual(atoi("words 42"), 0)
        self.assertEqual(atoi("42 words"), 42)
        self.assertEqual(atoi("3333333333333333333333333333333"), 2147483647)
        self.assertEqual(atoi("-3333333333333333333333333333333"), -2147483648)
        self.assertEqual(atoi(" -1010023630o4"), -1010023630)
if __name__ == "__main__":
    unittest.main()


