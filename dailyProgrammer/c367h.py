'''

"Fit non-congruent rectangles into a n*n square grid. What is the smallest difference possible between the areas of the largest and the smallest rectangles?"

Ex. given a 3 x 3 grid, you can fit 

1 0 0
1 0 0
2 2 2

so the smallest possible difference is 2 = 4 - 2. 

The rectangles must be distinct, so a 8 x 1 is the same as a 1 x 8. 

Important considerations:
 - Factoring allows multiple pieces of the same area.
 - the pieces must be able to be put together into a n x n rectangle.

Idea for the second constraint:
 - Pick rectangles that result in the canvas becoming another rectangle.
 
Ex. given the 3 x 3 grid,

2 2 2 would be taken first, because it results in a 2 x 3 grid:
1 1 or 0 0 can be taken next, because that is still a rectangle
       0 0 
Last piece taken as is, because subdividing further results in repeating pieces.

Rephrase problem statement:

Given a n x m canvas, and used pieces P, is it possible to fit non-congruent pieces into the n x m canvas?

Refinement of second constraint:

Given a n x m canvas, and used pieces P, extract pieces P2 from either canvas n x k or m x k, such that P2 form canvas n x k or m x k, 
and none of the pieces in P2 are in P. 

This is a dynamic programming problem

OPT(n, m) = min { min_{1 <= k <= n} { OPT(k, m) + OPT(n - k, m) }
                  min_{1 <= k <= m} { OPT(n, k) + OPT(n, m - k) } }
or some variant of this recurrence

There are two components to think about while doing this recurrence: if it is possible to break the figure into two rectangles in this manner, and if it is, to minimize the difference in pieces 

OPT(n, m, P) because we need to keep track of pieces used. 

Let arr[n][m] be an array of all the possible pieces needed to create a n x m rectangle
 
Ex. [ {(n,m)}, {(n-1,m), (1,m)} ... ]


'''
import math

def filtered_set_union(a, b):
    working_list = []
    for item in a:
        # assume that we are using item (which is a set)
        for other in b:
            # no repeating elements in either set
            print item.intersection(other)
            if item.intersection(other) == set():
                working_list.append(item.union(other))
                
    return working_list

def mondrian_puzzle(n):
    arr = [ [ [] for i in range(n+1) ] for row in range(n+1) ]
    
    for i in range(n):
        # convention about rectangles, left <= right term.
        arr[1][i].append(set([(1,i)]))
        arr[i][1].append(set([(1,i)]))
        

    for i in range(1,n+1):
        for j in range(i,n+1):
            # i, j can be broken into several components, from 1 to i, and 1 to j rectangles
            
            working_list = [] 
            for k in range(1, int(math.floor(i/2))+1):
                # choose sets from arr[k][m], arr[n-k][m] that are possible
                set_res = filtered_set_union(arr[k][j], arr[i-k][j])
                if set_res != []:
                    working_list.extend(set_res)
            for k in range(1, int(math.floor(j/2))+1):
                set_res = filtered_set_union(arr[i][k], arr[i][j-k])
                if set_res != []:
                    working_list.extend(set_res)
            
            working_list.append(set([(i,j)]))
            print "%d, %d"%(i,j)
            print working_list
            
            arr[i][j] = working_list
    
    return arr


import unittest
class TestMondrian(unittest.TestCase):
    def test_filtered(self):
        self.assertEqual(filtered_set_union([set([(1,2)])], [set([(1,2)])]), [])
        self.assertEqual(filtered_set_union([set([(1,2)])], [set([(2,2)])]), [set([(1,2),(2,2)])])
    def test_mondrian(self):
        self.assertEqual(mondrian_puzzle(3), [])


if __name__ == "__main__":
    unittest.main()
