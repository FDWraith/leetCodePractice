'''

Problem: Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

'''

def palindrome_num(n):
    """
    n - integer
    ret: boolean
    """
    if (n < 0):
        return False
    
    reverse_num = 0
    num = n
    while (num > 0):
        """
        reverse_num = 10 * reverse_num + num % 10
        num /= 10
        """
        # interesting observation, the above runtime is much slower than the one belwo
        reverse_num = (10 * reverse_num) + (num % 10)
        num = num / 10
    
    return n == reverse_num

import unittest

class testPalindromeNumber(unittest.TestCase):
    def test_palidrome_num(self):
        self.assertEqual(palindrome_num(121), True)
        self.assertEqual(palindrome_num(-121), False)
        self.assertEqual(palindrome_num(1213), False)
        self.assertEqual(palindrome_num(10), False)
        self.assertEqual(palindrome_num(101), True)
        

if __name__ == "__main__":
    unittest.main()
