'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
'''

def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    nextNumIdx = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[nextNumIdx] = nums[nextNumIdx], nums[i]
            nextNumIdx += 1


print(moveZeroes([0,1,0,3,12]))
print(moveZeroes([0]))

'''
All we need is to keep track of where the current zero and the next non-zero number is, then swap them. 
J increments every time until a zero is encountered, which means j will be at where the first zero is
'''