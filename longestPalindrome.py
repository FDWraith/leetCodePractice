def longestPalindrome(s):
    """
    Finds the longest palindrome in the string s
    
    Key Arguments:
    s -- string
    """

    longestP = ""
    
    
    # possible solution is to bash out every single length of string, 
    # with a helper method to determine if each length of string is palindromic
    # and then return the longest one.

    # we could work backwards: check each series of strings for the longest palindrome
    # that's recursive, and probably still super inefficient??

    # Here's how it would work:
    # "abab"
    # tries "abab" and sees it's not a palindrome. It then tries to find longest
    # of "aba" and "bab", and sees that they're both palindromes. It picks leftmost one.
    # this would need a helper method: isPalindromic(s), and the solution in the worst case, would 
    # have O(n^n) runtime, but in the best case, would be O(n)

    # let's try it
    '''
    if isPalindromic(s):
        return s
    else:
        s1 = longestPalindrome(s[:-1])
        s2 = longestPalindrome(s[1:])
        
        if len(s2) > len(s1):
            return s2
        else:
            return s1
    '''
    # Definitely a bad idea

    # That's not good enough, in the test case "abaddddd", it would have to try
    # "baddddd", "abadddd", "abaddd", "badddd", "addddd" before it gets to "ddddd"

    # let's try expanding around each possible palindrome center
    
    start = 0
    end = 0
    
    for index in range(0, len(s)):
        len1 = expandAroundCenter(s, index, index)
        len2 = expandAroundCenter(s, index, index + 1)
        length = max(len1, len2)
        
        # if newly computed palindrome is longer than current longest
        # replace the old longest with new
        if (length > end - start):
            start = index - (length - 1) / 2
            end = index + (length / 2)
    
    return s[start:end+1]

    
def isPalindromic(s):
    """Determines if s is palindromic, and returns True/False"""
    list = s
    for index in range(0,len(list)/2):
        charLeft = list[index]
        charRight = list[len(list)-index-1]
        if charLeft != charRight:
            return False
    return True


def expandAroundCenter(s, left, right):
    """
    Computes the length of the longest palindrome in @s, given that the
    center of the palindrome is between @left and @right
    """
    L = left
    R = right

    while (L >= 0 and R < len(s) and s[L] == s[R]):
        L -= 1
        R += 1
   
    return R - L - 1



# Tests
import unittest

class TestPalidrome(unittest.TestCase):
    def test_isPalindromic(self):
        self.assertEqual(isPalindromic("a"), True)
        self.assertEqual(isPalindromic("aba"), True)
        self.assertEqual(isPalindromic("hello"), False)
        
    def test_expandAroundCenter(self):
        self.assertEqual(expandAroundCenter("a",0,0), 1)
        self.assertEqual(expandAroundCenter("aa",0,1), 2)
        self.assertEqual(expandAroundCenter("aba",1,1), 3)
        self.assertEqual(expandAroundCenter("aba",2,2), 1)
        
  
    def test_longestPalidrome(self):
        self.assertEqual(longestPalindrome("aba"), "aba")
        self.assertEqual(longestPalindrome("ab"), "b")
        self.assertEqual(longestPalindrome("abaddddd"), "ddddd")
        self.assertEqual(longestPalindrome("abdcdadfrgjiajfdklajfieoajblalb"), "blalb")

if __name__ == "__main__":
    unittest.main()
