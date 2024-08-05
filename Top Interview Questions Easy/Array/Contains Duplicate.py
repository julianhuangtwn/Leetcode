'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
'''


def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    uniqueNums = set()
    for num in nums:
        if num not in uniqueNums:
            uniqueNums.add(num)
        else:
            return True
    return False


print(containsDuplicate([1,2,3,1]))
print(containsDuplicate([1,2,3,4]))
print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))


'''
We can make this O(n) complexity by just going through the list once (worst case having to travel through the entire array)
Add each number we see to a set, a set cannot contain duplicate numbers so it is useful in this case
'''