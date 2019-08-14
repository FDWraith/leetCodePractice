"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
"""

def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    productsBefore = [ 1 for n in nums ]
    productSoFar = 1
    for (i, n) in enumerate(nums):
        productsBefore[i] = productSoFar
        productSoFar *= nums[i]
        
    productsAfter = [ 1 for n in nums ]
    productSoFar = 1
    for i in range(len(nums)):
        productsAfter[len(nums) - i - 1] = productSoFar
        productSoFar *= nums[len(nums) - i - 1]
        
    results = []
    for i in range(len(nums)):
        results.append(productsBefore[i] * productsAfter[i])
            
    return results

def productExceptSelfSpaceOptimized(nums):
    
    results = [ 1 for n in nums ]
    
    leftProduct = 1
    for i in range(len(nums)):
        results[i] = leftProduct
        leftProduct *= nums[i]
    
    rightProduct = 1
    for i in range(len(nums)):
        results[len(nums) - i -1] *= rightProduct
        rightProduct *= nums[len(nums) - i - 1]

    return results

# Testing
print "Actual: " + str(productExceptSelf([1,2,3,4])) + ", Expected: [24, 12, 8, 6]"
print "Actual: " + str(productExceptSelf([1,2,3,0])) + ", Expected: [0, 0, 0, 6]"
print "Actual: " + str(productExceptSelf([1,1,1,1])) + ", Expected: [1, 1, 1, 1]"
print "Actual: " + str(productExceptSelf([-1,2,-3,4,-5])) + ", Expected: [120, -60, 40, -30, 24]"
print "-----------------------------"
print "Actual: " + str(productExceptSelfSpaceOptimized([1,2,3,4])) + ", Expected: [24, 12, 8, 6]"
print "Actual: " + str(productExceptSelfSpaceOptimized([1,2,3,0])) + ", Expected: [0, 0, 0, 6]"
print "Actual: " + str(productExceptSelfSpaceOptimized([1,1,1,1])) + ", Expected: [1, 1, 1, 1]"
print "Actual: " + str(productExceptSelfSpaceOptimized([-1,2,-3,4,-5])) + ", Expected: [120, -60, 40, -30, 24]"
