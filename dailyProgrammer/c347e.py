'''

Subfactorial (derangement)

!1 = 0, because {1} can't change its positions around
!2 = 1, because {1, 2} becomes {2, 1}, but can't move around anymore
!3 = 2, because {1, 2, 3} can either become {3, 1, 2} or {2, 3, 1}

Examine !3:
{1, 2, 3}

{3, 1, 2}
{2, 3, 1}

Nothing comes from previous cases...

2 * (!2) ?

Examine !4:
{1, 2, 3, 4}

{4, 1, 2, 3}
{4, 3, 1, 2} *
{4, 3, 2, 1}

{3, 4, 2, 1}
{3, 1, 4, 2}
{3, 4, 1, 2}

{2, 3, 4, 1}
{2, 4, 1, 3}
{2, 1, 4, 3}

Only the asterick comes from previous case...

How can I reconstruct !4 in terms of !3, and should I?

3 * (!3) + 1 ?

!3 : 2 * (!2) + 2 * (!1) ? check
!4 : 3 * (!3) + 3 * (!2) ? check 
!5 : 4 * (!4) + 4 * (!3) ? check
!6 : 5 * (!5) + 5 * (!4) ? check

Alternatively, let's examine 3!

{1, 2, 3}
{1, 3, 2}
{2, 1, 3}
{2, 3, 1} *
{3, 1, 2} *
{3, 2, 1} 


'''
def defragment(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return (n-1) * (defragment(n-1) + (defragment(n-2)))

# Tests
import unittest

class TestDegragment(unittest.TestCase):
    
    def test_degragment(self):
        self.assertEqual(defragment(1), 0)
        self.assertEqual(defragment(4), 9)
        self.assertEqual(defragment(5), 44)
        self.assertEqual(defragment(9), 133496)
        self.assertEqual(defragment(14), 32071101049)

if __name__ == "__main__":
    unittest.main()
