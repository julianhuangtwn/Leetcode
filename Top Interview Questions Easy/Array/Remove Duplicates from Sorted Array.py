'''
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

 

Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
 

Constraints:

1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.
'''

def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    uniquePtr = 0
    for i in range(len(nums)):
        if nums[i] != nums[uniquePtr]:
            uniquePtr += 1
            nums[uniquePtr], nums[i] = nums[i], nums[uniquePtr]
    
    return uniquePtr + 1


print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]));


'''
Since we need to do inplace, we can make this so that it keeps track of which index to swap with, and the loop itself with i to keep track of where we are in the array
Then we just have to check whether we find a different number or not. 
We don't have to worry about the case where we should check previously stored unique numbers as this array is promised to be non decreasing order
'''