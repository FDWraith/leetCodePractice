def convert(s, rows):
    """
    Converts the string @s into a zig zag with @rows rows, and then returns the resulting
    string when read from left to right

    Ex.
    helloworld, 3 -->
    H   O   L
    E L W R D
    L   O
    --> holelwrdlo
    """
    
    # Ideas
    
    # There's clearly some math involved in this problem, because the diagonals are limited by rows
    # In the first example, 3 letters separate each charater in the first row "h"ell"o"wor"l"d
    
    # Let's see some more complex examples
    
    '''
    theinternational, 4 -->

    T     E     O
    H   T R   I N
    E N   N T   A
    I     A     L
    
    --> teohtrinenntaial
    
    expansiveworldbuilding, 5 -->
    
    E       E       I
    X     V W     U L
    P   I   O   B   D
    A S     R D     I G
    N       L       N

    --> eeixvwulpiobdasrdignln
    '''
    
    # the separation goes from like so: 3, 5, 7, which is 2 * (r-2) + 1
    
    # second row
    # we still have the same dist of separation, such as h"e"llo"w"orl"d"
    # but we also get some additional characters, which are hel"l"wo"r"ld
    # which is 1 character seperated from the 2nd row characters
    
    # in 4 rows, it's 3 
    # in 5 rows, it's 5
    
    # let n be the nth row (counting from 0)
    # let r be the number of rows total
    # then, the characters in the nth row are
    # n, n + [2 * (r-2) + 1], n + 2[2 * (r-2) + 1] ...
    # and n + [2 * (r-n-2) + 1], n + [2 * (r-n-2) + 1] + [2 * (r-2) + 1] ...
    
    # okay... now that we have the math down, let's code it

    endString = ""
    if (rows == 1):
        return s
    for n in range(0, rows):
        rowString = ""
        sep = 2 * (rows - 2) + 2 
        # first and last row don't have any displacement
        displs = 0 if n == rows - 1 or n == 0 else 2 * (rows - n - 2) + 2
        k = 0
        
        while (n + k * sep < len(s) or n + displs + k * sep < len(s)):
            if (n + k * sep < len(s)):
                rowString += s[n + k * sep]
            if (n + displs + k * sep < len(s)):
                rowString += s[n + displs + k * sep]
           
            # if it's first or last row, I have a repeating element
            if (displs == 0):
                rowString = rowString[:-1]
               
            k += 1
        endString += rowString
    return endString
    
    

# Tests
import unittest

class TestZigZag(unittest.TestCase):
    def test_convert(self):
        self.assertEqual(convert("a", 1), "a")
        self.assertEqual(convert("helloworld", 3), "holelwrdlo")
        self.assertEqual(convert("theinternational", 4), "teohtrinenntaial")
        self.assertEqual(convert("expansiveworldbuilding", 5), "eeixvwulpiobdasrdignln")

if __name__ == "__main__":
    unittest.main()
    
