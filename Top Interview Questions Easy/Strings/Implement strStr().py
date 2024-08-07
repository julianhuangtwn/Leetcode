'''
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
'''

def strStr(haystack: str, needle: str) -> int:
    if len(needle) > len(haystack):
        return -1
    for i in range(len(haystack)):
        if haystack[i] == needle:
            return i
        elif i + len(needle) > len(haystack):
            return -1
        elif haystack[i:i + len(needle)] == needle:
            return i
    return -1


'''
Utilize slicing to get a substring and compare it with needle
Consider special cases where needle is already longer than haystack,
or there is only one letter
or account for out of range
'''