'''
You are given an array nums consisting of positive integers.

Return the total frequencies of elements in nums such that those elements all have the maximum frequency.

The frequency of an element is the number of occurrences of that element in the array
'''

from collections import Counter

def maxFrequencyElements(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0;
        nums.sort()
        
        frequencyList = Counter(nums)
        
        maxFreq = max(frequencyList.values())
        
        for i in frequencyList.values():
            if (maxFreq == i):
                count += maxFreq
                
        
        return count

'''
Input: nums = [1,2,2,3,1,4]
Output: 4
Explanation: The elements 1 and 2 have a frequency of 2 which is the maximum frequency in the array.
So the number of elements in the array with maximum frequency is 4.
'''
print(maxFrequencyElements([1,2,2,3,1,4]))

'''
Input: nums = [1,2,3,4,5]
Output: 5
Explanation: All elements of the array have a frequency of 1 which is the maximum.
So the number of elements in the array with maximum frequency is 5.
'''
print(maxFrequencyElements([1,2,3,4,5]))