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
    '''
    :type nums: List[int]
    :rtype: List[int]
    '''
        
    sum = 0
    result = []
    # Go through the nums array
    for num in nums:
        # sum will add the current index num in nums
        sum += num
        # add the sum to the result array
        result.append(sum)
    return result

print(runningSum([1,2,3,4,5]))

'''
While this code passed, this was only 50% faster than other submissions

Reviewing the code, we might not have to recreate another array to save memory space and time, 
also, realizing that sum can start from the first element, and we can always just add the previous
element in the modified array, as the previous number is always the sum of all previous elements
'''

