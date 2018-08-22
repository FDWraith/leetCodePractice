def longestPalindrome(s):
    """
    Finds the longest palindrome in the string s
    
    Key Arguments:
    s -- string
    """

   
# Tests
import unittest

class TestPalidrome(unittest.TestCase):
    
    def test_longestPalidrome(self):
        self.assertEqual(longestPalindrome("aba"), "aba")
        self.assertEqual(longestPalindrome("ab"), "a")
        self.assertEqual(longestPalindrome("abaddddd"), "ddddd")

if __name__ == "__main__":
    unittest.main()
