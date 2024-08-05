'''
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
 

Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
'''

def intersect(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    numCount = {}
    result = []
    for num in nums1:
        if num in numCount:
            numCount[num] += 1
        else:
            numCount[num] = 1
            
    for num in nums2:
        if num in numCount and numCount[num] > 0:
            numCount[num] -= 1
            result.append(num)
    
    return result


print(intersect([1,2,2,1], [2,2]))
print(intersect([4,9,5], [9,4,9,8,4]))

    
'''
We utilize a hashmap/dictionary to store key value pairs to count the occurrence of each number
Then we can access the second list and "extract" any numbers found as the key, effectively getting a list of intersected numbers

If the lists are sorted, we can then just use a double pointer, as this method we can just compare the two arrays one by one at the same number
without having to use extra space for the hashmap
'''

def intersectSorted(nums1, nums2):
    result = []
    i, j = 0

    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            result.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1

    return result

print(intersect([1,1,2,2], [2,2]))
print(intersect([4,5,9], [4,4,8,9,9]))


'''
As both methods require traversal through both lists with are O(n + m) complexities
We should use hashmap if nums1 is much smaller, since double pointers have much more operations going through j += 1
whereas hashmap we can finish the dictionary quickly for nums1, then just travel through nums2


If nums2 is stored on a disk, we may process nums2 in small sections so that we don't exceed memory storage
'''