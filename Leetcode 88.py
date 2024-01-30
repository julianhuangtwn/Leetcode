'''
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]...nums[i]).

Return the running sum of nums.

Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]

Constraints:

1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6
'''

def runningSum(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    
    '''
    Goes through the array from first index, adds the current index
    # with the previous index, as the previous index will always be the
    sum of all elements up to that index position
    '''
    for num in range(1, len(nums)):
        nums[num] += nums[num - 1]
    return nums

print(runningSum([1,2,3,4,5]))

'''
This code passed 99.86% of submissions. As this runs in linear time
O(n) once through the list and only the original list. As each index will
be updated with the sum of all numbers before the current index, we just
have to add the current index with the previous index to get the running
sum. The old solution with a brand new list and a sum variable is deleted.
'''

