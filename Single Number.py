'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
 

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
'''

def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    uniqueNum = 0
    for num in nums:
        uniqueNum ^= num
    
    return uniqueNum


print(singleNumber([2,2,1]))
print(singleNumber([4,1,2,1,2]))
print(singleNumber([1]))


'''
Using XOR operator ^ can help with finding the unique number as it is promised to be only one
XOR has the properties of cancelling the same number out to 0, and since it is a commutative operator, 
it doesn't matter to have to XOR the numbers in a certain order, we will always be left with the unique number at the end
as all duplicates cancel each other out after XOR operation
'''