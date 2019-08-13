"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

"""
Test Cases:

[-1, 0, 1] => [ [-1, 0, 1] ]
[-1, 0, -1] => [ ]
[-1, -1, 0, 0, 1, 1] => [ [-1, 0, 1] ]
[-1, -1, 0, 0, 1, 2] => [ [-1, 0, 1], [-1, -1, 2] ]
[-1, 0, 1, -1, 2, 0, 0, 1, -2] => [ [-1, 0, 1], [-1, -1, 2], [1, 1, -2], [0, 0, 0], [2, 0, -2] ]
[ 0, 0, 0, 0 ] => [ [0, 0, 0] ]

Obvious solution: Create sums of every possible triplet, and then remove duplicate triplets

Slightly more clever: Create sums of every unique duo, and use a map to figure out the triplet (if it exists). Still have to remove duplicates...

How to create sums of every unique duo:
[-1, 0, 1] => [ [-1, 0], [-1, 1], [0, 1] ]
           => this would generate the same triplet... three times

Cleverer: We can be slightly greedy about this (search in only one direction, because anything that came before is already part of a triplet)
          => Sort, and remove any exceess that appears more than 3 times
          => Create pairs, and then search to the right
          -- Still O(n^3 + nlogn), but we get rid of removing duplicates

Different Approach: Create two "pools", negatives + positives (+ zeroes are in both pools)
          => For every negative number, see if there are 2 positive numbers that can counter it
          => For every positive number, do the same to the negatives
          => The only duplicates will be the ones with zeros in them. 
Optimization is to take zeroes out of the pools
          => if there are at least 3 zeros, [0,0,0] is part of the solution
          => for any positive number, if there is a negative counterpart, and zero exists, then [+, 0, -] is a solution
Further optimization is to create 4 pools, negatives, positives, sum of 2 negs, sum of 2 pos

Runtime is O(n^2 + n) to create all of the pools. Pools are maps, so searching them is constant runtime
"""

def sum3(narr):
    zeroPool = [ n for n in narr if n == 0 ]
    negPool = { n : 0 for n in narr if n < 0 }
    posPool = { n : 0 for n in narr if n > 0 }
    
    for n in narr:
        if (n < 0):
            negPool[n] += 1
        elif (n > 0):
            posPool[n] += 1
    
    posPoolKeys = posPool.keys()
    posSumPool = {}
    for (aIndex, a) in enumerate(posPoolKeys):
        for b in posPoolKeys[aIndex:]:
            if (a != b or posPool[a] >= 2):
                if (a+b) in posSumPool:
                    posSumPool[a+b].append([a, b])
                else:
                    posSumPool[a+b] = [ [a, b] ]
    negPoolKeys = negPool.keys()
    negSumPool = {}
    for (aIndex, a) in enumerate(negPoolKeys):
        for b in negPoolKeys[aIndex:]:
            if (a != b or negPool[a] >= 2):
                if (a+b) in negSumPool:
                    negSumPool[a+b].append([a, b])
                else:
                    negSumPool[a+b] = [ [a, b] ]
    
    solution = []
    numOfZeroes = len(zeroPool)
    if numOfZeroes >= 3:
        solution.append( [0, 0, 0] )
    
    for neg in negPoolKeys:
        search = -1 * neg
        if search in posSumPool:
            for sumNums in posSumPool[search]:              
                solution.append( [neg] + sumNums )
        if numOfZeroes > 0 and search in posPool:
            solution.append( [neg, 0, search] )

    for pos in posPoolKeys:
        search = -1 * pos
        if search in negSumPool:
            for sumNums in negSumPool[search]:
                solution.append( [pos] + sumNums )
       
    return solution


# Testing
print "Actual: " + str(sum3([1, 0, -1])) + ", Expected: [ [1, 0, -1] ]"
print "Actual: " + str(sum3([0])) + ", Expected: []"
print "Actual: " + str(sum3([1, 0, -1, -1, 2])) + ", Expected: [ [1, 0, -1], [-1, -1, 2] ]"
print "Actual: " + str(sum3([0, 0, 0, 0])) + ", Expected: [ [0, 0, 0] ]"
print "Actual: " + str(sum3([1, 0, -1, 1, 0, -1, 2, -2, 0])) + ", Expected: [ [1, 0, -1], [1, 1, -2], [-1, -1, 2], [0, 0, 0], [2, 0, -2] ]"
print "Actual: " + str(sum3([-4, 2, 2, 3, 1])) + ", Expected: [ [-4, 2, 2], [-4, 3, 1] ]"
print "Actual: " + str(sum3([4, -2, -2, -3, -1])) + ", Expected: [ [4, -2, -2], [4, -3, -1] ]"

print "---------------------------------------------------"

"""
So that worked. 

Except this solution is too expensive space wise, and I seem to have over thought it.

Back to the clever approach, but with one optimization:
When 2Sum'ing the rest of the array, you can use two pointers to only loop through once

This brings solution down to O(n^2 + nlog(n))
"""

def sum3Alt(narr):
    narr.sort()
    
    solution = []
    prevVal = None
    while (len(narr) >= 3):
        val = narr[0]
        narr = narr[1:]
        
        if val == prevVal: 
            continue
        
        leftIndex = 0
        rightIndex = len(narr) - 1
        
        while (leftIndex < rightIndex):
            sumValue = val + narr[leftIndex] + narr[rightIndex]
            if (sumValue == 0):
                solution.append([val, narr[leftIndex], narr[rightIndex]])
                # move left and right indexes to new numbers
                while (leftIndex < rightIndex and narr[leftIndex] == narr[leftIndex + 1]):
                    leftIndex += 1
                while (leftIndex < rightIndex and narr[rightIndex] == narr[rightIndex - 1]):
                    rightIndex -= 1
                leftIndex += 1
                rightIndex -= 1
            elif (sumValue < 0):
                leftIndex += 1
            elif (sumValue > 0):
                rightIndex -= 1

        prevVal = val

    return solution


print "Actual: " + str(sum3Alt([1, 0, -1])) + ", Expected: [ [1, 0, -1] ]"
print "Actual: " + str(sum3Alt([0])) + ", Expected: []"
print "Actual: " + str(sum3Alt([1, 0, -1, -1, 2])) + ", Expected: [ [1, 0, -1], [-1, -1, 2] ]"
print "Actual: " + str(sum3Alt([0, 0, 0, 0])) + ", Expected: [ [0, 0, 0] ]"
print "Actual: " + str(sum3Alt([1, 0, -1, 1, 0, -1, 2, -2, 0])) + ", Expected: [ [1, 0, -1], [1, 1, -2], [-1, -1, 2], [0, 0, 0], [2, 0, -2] ]"
print "Actual: " + str(sum3Alt([-4, 2, 2, 3, 1])) + ", Expected: [ [-4, 2, 2], [-4, 3, 1] ]"
print "Actual: " + str(sum3Alt([4, -2, -2, -3, -1])) + ", Expected: [ [4, -2, -2], [4, -3, -1] ]"
