import math

# Problem Statement

# Reverse the digits of a 32-bit integer
# Bounds: [-2^32, 2^32 - 1]
# Overflow results in zero

def reverseInteger(num):
    """
    Reverses the digits of @num. Returns 0 if overflow
    """
    
    # I can't do this with just string reverse. I have to do this with an accumulator

    neg = num < 0
    num = abs(num)

    # Reversing a positive number, start from last digit, and accumulate the resulting number
    # Each time, check the resulting number for overflow. If it overflows, then return 0
    
    # @accumNum represents the reversedNumber so far
    accumNum = 0
   
    # At the end of this loop, accumNum is the reverse of num
    # Except: upon overflow, the function terminates and returns 0
    while num != 0: 
        lastDigit = num % 10
        num = num / 10 # python integer division
        
        accumNum = accumNum * 10 + lastDigit
        if accumNum >= math.pow(2, 32) and not neg:
            return 0
        elif accumNum > math.pow(2, 32) and neg:
            return 0

    return -1 * accumNum if neg else accumNum
        
        

    

# Tests
import unittest

class TestReverse(unittest.TestCase):
    def test_reverseInteger(self):
        self.assertEqual(reverseInteger(1), 1)
        self.assertEqual(reverseInteger(121), 121)
        self.assertEqual(reverseInteger(123), 321)
        self.assertEqual(reverseInteger(0), 0)
        self.assertEqual(reverseInteger(-1), -1)
        self.assertEqual(reverseInteger(-123), -321)
        self.assertEqual(reverseInteger(39999999999999), 0)

if __name__ == "__main__":
    unittest.main()
