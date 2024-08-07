'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
'''

from typing import List
def longestCommonPrefix(strs: List[str]) -> str:
    if not strs:
        return ''
    
    prefix = strs[0]
    for string in strs[1:]:
        while string[:len(prefix)] != prefix:
            prefix = prefix[:-1]
            if not prefix:
                return ''
    return prefix

print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["dog","racecar","car"]))


'''
As all the words need to match the prefix, we can just use the first string if it exists
Using slicing, we can keep sizing down until we match the largest part with the second string
This new prefix will then be matched against other strings in the list and keep sizing down 
Slicing is protected in the sense that it will not throw errors even if len(prefix) is too large, and just extract to the end of the string
'''